# nlp-sandbox-person-name-annotator-example

[![GitHub Stars](https://img.shields.io/github/stars/data2health/nlp-sandbox-person-name-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-person-name-annotator-example)
[![GitHub CI](https://img.shields.io/github/workflow/status/data2health/nlp-sandbox-person-name-annotator-example/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-person-name-annotator-example)
[![GitHub License](https://img.shields.io/github/license/data2health/nlp-sandbox-person-name-annotator-example.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/data2health/nlp-sandbox-person-name-annotator-example)

This Is the NLP Sandbox Person Name Annotation  Node.

## Introduction



## Specifications

TBA

## Deploy using Docker


1. Start the Data Node web service (RESP API)

        docker-compose up

2. In your browser, go to the web service documentation page
   <http://localhost:8080/api/v1/ui/> to check that the web service of the Data
   Node started successfully.

## Access logs

The current logs are saved to `/var/log/app/current`.

    $ docker exec data-node-api cat /var/log/app/current
    2020-09-25 23:33:39.809826500  Starting data node server
    2020-09-25 23:33:40.436453500   * Serving Flask app "__main__" (lazy loading)
    2020-09-25 23:33:40.436461500   * Environment: production
    2020-09-25 23:33:40.436462500     WARNING: This is a development server. Do not use it in a production deployment.
    2020-09-25 23:33:40.436463500     Use a production WSGI server instead.
    2020-09-25 23:33:40.436464500   * Debug mode: off

Follow the logs using `docker logs`

    docker logs --follow data-node-api

<!-- ## Deploy using Python (for development)

1. Install the dependencies

        pip install -r requirements.txt

2. Create the file that contains the future environment variables

        cp .env.sample .env

3. Set the configuration values in `.env` (see previous section)

4. Export the variables defined in *.env* to environment variables

        export $(grep -v '^#' .env | xargs -d '\n') -->

<!-- Definitions -->

[2014 i2b2 NLP De-identification Challenge]: https://www.i2b2.org/NLP/HeartDisease/