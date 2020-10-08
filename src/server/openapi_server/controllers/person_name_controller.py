import logging
from datetime import date
from flask import jsonify
import connexion
import spacy
import json
import datetime
from pprint import pprint

from openapi_server.models.note import Note
from openapi_server.models.person_name_annotation import PersonNameAnnotation  # noqa: E501
from openapi_server.utility.configuration import Config


def person_names_read_all(note=None):  # noqa: E501
    """Get all person name annotations

    Returns the person name annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[PersonNameAnnotation]
    """
    nlp = Config.nlp
    logging.info(f"NOTE TEXT: started")
    found = False
    counter = 1
    return_list = []
    if connexion.request.is_json:
        found = True
        note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        note_text = note[0]._text
        note_id = note[0]._id
        logging.info(f"NOTE TEXT: {note_text}")
        nlp = spacy.load('en_core_web_md')
        doc = nlp(note_text)
        for sent in doc.sents:
            for entity in sent.ents:
                logging.info(f"ENTITY found {entity} with label {entity.label_}")
                if entity.label_ == 'PERSON':
                    logging.info(f"{entity.text}  {entity.start_char} ")
                    return_list = add_match(counter, entity, note, return_list, note_id)
                    counter +=1
                    # logging.info(f"PRETTY : { pprint(return_list)}")

        for m in return_list:
            logging.info(f" text set to : {m.text}")

    return return_list


def add_match(counter, entity, note, returnList, note_id):
    if entity is not None:
        logging.info(f"Entity : {entity.text} found at {entity.start_char} ")
        da = PersonNameAnnotation(id=counter, created_by="Person Data Annotation Example",
                                  created_at=date.today() )
        # Set on Parent Class
        da.note_id = note_id
        da.text = entity.text
        da.start = entity.start_char
        returnList.append(da)
    else:
        logging.info(f"No Entity found")

    return returnList
