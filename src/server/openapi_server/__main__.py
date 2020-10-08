#!/usr/bin/env python3
import json

import connexion
import spacy

from openapi_server.models import PersonNameAnnotation
from openapi_server.utility.configuration import Config
from logging.config import dictConfig
from openapi_server import encoder

def main():
    # Set up logging
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    # Needed to Encode PersonNameEncoder classes as without it, the returned
    # array would not incllude the
    # Parent fields
    class PersonNameEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, PersonNameAnnotation):
                text = obj.text;  # From Parent Class, out of the box
                # connexion only returns fields on the child class
                created_date_str = obj.created_at.strftime("%y%m%d")
                note_id = obj.note_id
                start = obj.start
                return {'id': obj.id, 'note_id': note_id,
                        'createdBy': obj.created_by, 'text': text,
                        'created_at': created_date_str, "start": start}

            return json.JSONEncoder.default(self,
                                            obj)  # default, if not Delivery
            # object. Caller's problem if this is not serialziable.

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = PersonNameEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'NLP Sandbox Person Name Annotator API'},
                pythonic_params=True)

    Config.nlp
    app.run(port=8080)

if __name__ == '__main__':
    main()
