"""
Base abstract class for OCR services
"""
from abc import ABC, abstractmethod
from io import BytesIO


class OcrBase(ABC):
    """
    Base class to be
    """
    @abstractmethod
    def extract_text_from_image(self, image: BytesIO | str):
        """
        Load an image from a BytesIO element or a file path and tries to extract its text
        :param image:
        """
