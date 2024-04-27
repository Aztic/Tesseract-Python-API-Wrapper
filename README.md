# Tesseract Python API
Simple Python API wrapper for Tesseract OCR engine

## Requirements
- Python >= 3.11.8
- Tesseract >= 5.3.4

## Setup
```bash
git clone <repo url>
cd <repo>
python -m venv .venv --system-site-packages
source .venv/bin/activate
python -m pip install -r requirements.txt

cd app && python main.py
```
You can also directly use the docker image
```bash
docker build --build-args TESSERACT_LANGUAGES=spa,cat,ita -t tesseract-python-api .
docker run -p 8000:8000 tesseract-python-api
```
and consume the API at `http://localhost:8000`

## Test
```bash
pytest
```

## TODO
- Auth support
- Allow specify the language in the endpoint

## License
GPL-3.0. See [LICENSE](LICENSE) for more information.

## Why this wrapper?
I need some simple and generic OCR tool for my side projects. An API wrapper is an easy way to integrate it without
worrying about the implementation in the other projects.