#!/bin/bash

default_languages="${TESSERACT_LANGUAGES}"
languages_directory="${TESSDATA_DIR}"

if [ -z "$languages_directory" ]; then
    echo "Environment variable 'TESSDATA_DIR' is not set. Exiting."
    exit 1
fi

if [ -z "$default_languages" ]; then
    echo "Environment variable 'TESSERACT_LANGUAGES' is not set. Setting english as default"
    default_languages="eng"
fi

IFS=',' read -ra languages_to_download <<< "$default_languages"
for language in "${languages_to_download[@]}"; do
    echo "Downloading language: $language"
    curl -s "https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/${language}.traineddata" -o "${languages_directory}/${language}.traineddata"
done

final_languages=$(echo "$default_languages" | tr ',' '+')
echo "TESSERACT_DEFAULT_LANGUAGES=$final_languages" >> /code/app/.env