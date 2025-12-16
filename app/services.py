import logging
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("legacy_vault")

# Email configuration - supports Gmail SMTP (free) or SendGrid
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")  # Your Gmail address
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")  # Gmail App Password (NOT your regular password)
FROM_EMAIL = os.getenv("FROM_EMAIL")

# Optional SendGrid (if you prefer it later)
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


def send_email(to_email: str, subject: str, content: str):
    """
    Sends an email using:
    1. Gmail SMTP (if SMTP_USER/SMTP_PASSWORD configured) - FREE!
    2. SendGrid (if API key configured)
    3. Mock logger (fallback for development)
    
    Gmail Setup:
    1. Enable 2FA on your Google account
    2. Go to: https://myaccount.google.com/apppasswords
    3. Create an "App Password" for "Mail"
    4. Use that 16-char password as SMTP_PASSWORD
    """
    
    # Try Gmail SMTP first (FREE!)
    if SMTP_USER and SMTP_PASSWORD and "your_" not in SMTP_PASSWORD:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = FROM_EMAIL or SMTP_USER
            msg['To'] = to_email
            
            # Attach HTML content
            html_part = MIMEText(content, 'html')
            msg.attach(html_part)
            
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(msg['From'], to_email, msg.as_string())
            
            logger.info(f"Email sent via SMTP to {to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email via SMTP: {str(e)}")
            # Fall through to next method
    
    # Try SendGrid if configured
    if SENDGRID_API_KEY and "your_sendgrid" not in SENDGRID_API_KEY:
        try:
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            
            message = Mail(
                from_email=FROM_EMAIL,
                to_emails=to_email,
                subject=subject,
                html_content=content
            )
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            logger.info(f"Email sent via SendGrid to {to_email} | Status: {response.status_code}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email via SendGrid: {str(e)}")
    
    # Mock / Fallback for development
    logger.info(f"--- MOCK EMAIL (No SMTP configured) ---")
    logger.info(f"To: {to_email}")
    logger.info(f"Subject: {subject}")
    logger.info(f"Content: {content[:200]}...")
    logger.info(f"----------------------------------------")
    
    with open("email_log.txt", "a") as f:
        f.write(f"To: {to_email}\nSubject: {subject}\nContent: {content}\n---\n")
    return True
