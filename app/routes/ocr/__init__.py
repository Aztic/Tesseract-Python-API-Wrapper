"""
Router to handle anything related to OCR services
"""
from fastapi import APIRouter, UploadFile, HTTPException
from services.ocr import get_ocr

router = APIRouter()


@router.post('/get-text')
async def get_image_text(file: UploadFile):
    """
    Gets the text of the image
    :param file:
    :return:
    """
    try:
        ocr = get_ocr()
        text = ocr.extract_text_from_image(file.file)
        return {
            "text": text
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail={"error": "Could not extract the file information"}
        )
