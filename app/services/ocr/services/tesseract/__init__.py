import os
from io import BytesIO

import pytesseract
from PIL import Image
from services.ocr.base_ocr import OcrBase


class TesseractOcr(OcrBase):
    tesseract_initialized = False

    def __init__(self, languages: str | None = None):
        if not TesseractOcr.tesseract_initialized:
            TesseractOcr.set_tesseract_path(os.environ['TESSERACT_PATH'])
            TesseractOcr.tesseract_initialized = True
        if languages is not None:
            self.languages = languages
        else:
            self.languages = os.environ['TESSERACT_DEFAULT_LANGUAGES']

    def extract_text_from_image(self, image: BytesIO | str):
        """
        Extracts a text from a given image
        :param image:
        :return:
        """
        return pytesseract.image_to_string(Image.open(image), lang=self.languages)

    @staticmethod
    def set_tesseract_path(path: str):
        """
        Sets the path to the tesseract executable
        :param path:
        """
        pytesseract.pytesseract.tesseract_cmd = path
        TesseractOcr.tesseract_initialized = True
