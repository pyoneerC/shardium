import secrets
from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .database import SessionLocal, engine, Base
from .models import User
from .services import send_email

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shardium")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/vault/create", response_class=HTMLResponse)
async def create_vault(
    request: Request,
    email: str = Form(...),
    beneficiary_email: str = Form(...),
    shard_c: str = Form(...),
    db: Session = Depends(get_db)
):
    # Check if user exists
    user = db.query(User).filter(User.email == email).first()
    if user:
        return templates.TemplateResponse("index.html", {"request": request, "error": "User already exists with this email."})

    heartbeat_token = secrets.token_urlsafe(32)
    new_user = User(
        email=email,
        beneficiary_email=beneficiary_email,
        shard_c=shard_c,
        heartbeat_token=heartbeat_token,
        last_heartbeat=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # In a real app, we might email the user a confirmation link first.
    # Here we simulate the 'welcome' email which might include the first heartbeat link.
    send_email(email, "Welcome to Shardium", f"Your vault is active. We will check on you in 30 days. Your heartbeat link: http://localhost:8000/heartbeat/{new_user.id}/{heartbeat_token}")
    
    # Ideally User should have Shard B printed/PDFd. The form should have handled showing that.
    # The server just acknowledges receipt of Shard C.
    
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/heartbeat/{user_id}/{token}", response_class=HTMLResponse)
async def heartbeat(request: Request, user_id: int, token: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id, User.heartbeat_token == token).first()
    if not user:
        return HTMLResponse("Invalid link", status_code=404)
    
    user.last_heartbeat = datetime.now()
    user.is_dead = False # Resurrect if previously marked
    db.commit()
    
    return templates.TemplateResponse("check_in.html", {"request": request, "message": "Heartbeat confirmed. Timer reset for 30 days."})

@app.get("/recover", response_class=HTMLResponse)
async def recover_page(request: Request):
    return templates.TemplateResponse("recover.html", {"request": request})

# Internal endpoint to trigger death logic (Simulated cron job)
@app.post("/simulate/cron/check-deaths")
async def check_deaths(db: Session = Depends(get_db)):
    # Find users with last_heartbeat > 90 days (shortened to 1 minute for demo if needed, but sticking to logic)
    # For demo purposes, we'll allow a query param or just check everyone.
    # Let's say threshold is 90 days.
    threshold = datetime.now() - timedelta(days=90)
    dead_users = db.query(User).filter(User.last_heartbeat < threshold, User.is_dead == False).all()
    
    results = []
    for user in dead_users:
        user.is_dead = True
        send_email(
            user.beneficiary_email, 
            "URGENT: Shardium Activation", 
            f"We have not heard from {user.email} for 90 days. Here is Shard C: {user.shard_c}. Combine this with Shard B to recover the key."
        )
        results.append(f"Emailed beneficiary of {user.email}")
    
    db.commit()
    return {"processed": len(dead_users), "details": results}

