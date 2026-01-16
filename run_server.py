import uvicorn
import os
import sys

# Ensure the current directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("Starting Deadhand Server...")
    print("Visit http://127.0.0.1:8000 in your browser.")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
