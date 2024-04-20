"""
API to interact with an ocr service
"""

from fastapi import FastAPI
from routes import register_routes
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
register_routes(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
