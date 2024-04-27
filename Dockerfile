FROM ubuntu:24.04 AS setup
ENV PIP_BREAK_SYSTEM_PACKAGES=1
RUN apt update && apt install -y tesseract-ocr curl python3.12 python3.12-venv
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.12 get-pip.py
RUN mkdir -p /content/tessdata
ENV TESSDATA_DIR=/content/tessdata
ENV TESSDATA_PREFIX=/content/tessdata
ENV TESSERACT_PATH=/usr/bin/tesseract
ARG TESSERACT_LANGUAGES='eng,spa,cat'
ENV TESSERACT_LANGUAGES=$TESSERACT_LANGUAGES


FROM setup AS setup-app
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python3.12 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN rm -f ./code/app/.env

FROM setup-app AS configure
COPY ./scripts /content/scripts
RUN chmod +x /content/scripts/setup_languages.sh
RUN /content/scripts/setup_languages.sh

FROM configure AS run
CMD ["python3.12", "/code/app/main.py"]
EXPOSE 8000