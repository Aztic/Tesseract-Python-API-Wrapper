FROM ubuntu:22.04 AS setup
RUN apt update && apt install -y tesseract-ocr curl python3.11 python3.11-venv
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.11 get-pip.py
RUN mkdir -p /content/tessdata
ENV TESSDATA_DIR=/content/tessdata

FROM setup AS configure
WORKDIR /content/tessdata
RUN curl https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata -o eng.traineddata
RUN curl https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata -o spa.traineddata
RUN curl https://github.com/tesseract-ocr/tessdata_best/raw/main/cat.traineddata -o cat.traineddata


# Python image
FROM configure AS setup-python
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python3.11 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["python3.11", "/code/app/main.py"]
EXPOSE 8000


