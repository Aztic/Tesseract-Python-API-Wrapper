from unittest.mock import patch
from services.ocr.services.tesseract import TesseractOcr
TesseractOcr.tesseract_initialized = True


def setup_env() -> dict:
    return {
        'TESSERACT_PATH': '/usr/bin/tesseract',
        'TESSERACT_DEFAULT_LANGUAGES': 'eng+spa+cat'
    }


def test_tesseract_uses_provided_language():
    with (
        patch('services.ocr.services.tesseract.os') as mock_os,
        patch('services.ocr.services.tesseract.Image') as mock_image,
        patch('services.ocr.services.tesseract.pytesseract') as mock_pytesseract
    ):
        # Arrange
        language = 'fra'
        mock_os.environ = setup_env()
        tesseract = TesseractOcr(language)
        image_path = ''

        # Act
        tesseract.extract_text_from_image(image_path)

        # Assert
        assert mock_pytesseract.image_to_string.called_with(
            mock_image.open(image_path),
            lang=language
        )


def test_tesseract_falls_back_to_default_language_when_no_language_provided():
    with (
        patch('services.ocr.services.tesseract.os') as mock_os,
        patch('services.ocr.services.tesseract.Image') as mock_image,
        patch('services.ocr.services.tesseract.pytesseract') as mock_pytesseract
    ):
        # Arrange
        env_values = setup_env()
        language = env_values['TESSERACT_DEFAULT_LANGUAGES']
        mock_os.environ = env_values
        tesseract = TesseractOcr()
        image_path = ''

        # Act
        tesseract.extract_text_from_image(image_path)

        # Assert
        assert mock_pytesseract.image_to_string.called_with(
            mock_image.open(image_path),
            lang=language
        )
