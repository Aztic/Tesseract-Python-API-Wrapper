"""
Central ocr service to be imported by other modules
"""
from services.ocr.services.tesseract import TesseractOcr


def get_ocr():
    """
    Returns the OCR service
    :return:
    """
    return TesseractOcr()
