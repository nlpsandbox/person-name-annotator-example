FROM python:3.8.5-slim-buster
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        curl \
        unzip \
        vim \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt \
    &&  python3 -m spacy download en_core_web_md

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]