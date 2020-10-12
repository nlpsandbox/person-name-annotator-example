# OpenAPI generated server

## Overview
This server was generated by the [OpenAPI Generator](https://openapi-generator.tech) project. By using the
[OpenAPI-Spec](https://openapis.org) from a remote server, you can easily generate a server stub.  This
is an example of building a OpenAPI-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_md
python3 -m openapi_server
```

one can optionally set these ENV variables:

export FLASK_ENV=development
export FLASK_PORT=8080


and open your browser to here:

```
http://localhost:8080/api/v1/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/api/v1/openapi.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker_compose  build  

# starting up a container
docker_compose up

```