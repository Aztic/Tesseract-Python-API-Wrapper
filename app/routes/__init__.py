"""
Central router handler
"""
from fastapi import FastAPI
from routes.ocr import router as ocr_router


def register_routes(app: FastAPI):
    """
    Register all routes for the app
    :param app:
    """
    app.include_router(prefix='/ocr', router=ocr_router)
