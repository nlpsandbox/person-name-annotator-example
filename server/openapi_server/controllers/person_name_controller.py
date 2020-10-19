import logging
from datetime import date
from flask import jsonify
import connexion
import spacy
import json
import datetime
from pprint import pprint
import csv
import os.path
from os import path

from openapi_server.models.note import Note
from openapi_server.models.person_name_annotation import \
    PersonNameAnnotation  # noqa: E501
from openapi_server.utility.configuration import Config


def person_names_read_all(note=None):  # noqa: E501
    """Get all person name annotations

    Returns the person name annotations # noqa: E501

    :param note:
    :type note: list | bytes

    :rtype: List[PersonNameAnnotation]
    """
    res = []

    # with open('') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #             line_count += 1
    #     print(f'Processed {line_count} lines.')


    # if connexion.request.is_json:
    #     notes = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

    #     for note in notes:
    print("plop")
    if path.exists("data/census_gov_top_1000_lastnames.csv"):
        logging.info("CSV EXISTS")
    else:
        logging.info("CSV DOES NOT EXIST")


            # # Adapted from https://stackoverflow.com/a/61234139
            # matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(/)([1-9]|0[1-9]|1[0-2])(/)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            # add_date_annotation(res, note, matches, "MM/DD/YYYY")

            # matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-)([1-9]|0[1-9]|1[0-2])(-)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            # add_date_annotation(res, note, matches, "MM-DD-YYYY")

            # matches = re.finditer('([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.)([1-9]|0[1-9]|1[0-2])(\.)(19[0-9][0-9]|20[0-9][0-9])', note._text)
            # add_date_annotation(res, note, matches, "MM.DD.YYYY")

            # matches = re.finditer('([1-9][1-9][0-9][0-9]|2[0-9][0-9][0-9])', note._text)
            # add_date_annotation(res, note, matches, "YYYY")

            # matches = re.finditer('(January|February|March|April|May|June|July|August|September|October|November|December)', note._text, re.IGNORECASE)
            # add_date_annotation(res, note, matches, "MMMM")

            # # TODO: Remove annotations that are fully included into another
            # # annotation.

    return jsonify(res)
    # nlp = Config.nlp
    # logging.info(f"NOTE TEXT: started")
    # found = False
    # counter = 1
    # return_list = []
    # if connexion.request.is_json:
    #     found = True
    #     note = [Note.from_dict(d) for d in
    #             connexion.request.get_json()]  # noqa: E501
    #     note_text = note[0]._text
    #     note_id = note[0]._id
    #     logging.info(f"NOTE TEXT: {note_text}")
    #     nlp = spacy.load('en_core_web_md')
    #     doc = nlp(note_text)
    #     for sent in doc.sents:
    #         for entity in sent.ents:
    #             logging.info(
    #                 f"ENTITY found {entity} with label {entity.label_}")
    #             if entity.label_ == 'PERSON':
    #                 logging.info(f"{entity.text}  {entity.start_char} ")
    #                 return_list = add_match(counter, entity, note, return_list,
    #                                         note_id)
    #                 counter += 1
    #                 # logging.info(f"PRETTY : { pprint(return_list)}")

    #     for m in return_list:
    #         logging.info(f" text set to : {m.text}")

    # return return_list


def add_match(counter, entity, note, returnList, note_id):
    if entity is not None:
        logging.info(f"Entity : {entity.text} found at {entity.start_char} ")
        da = PersonNameAnnotation(id=counter,
                                  created_by="Person Data Annotation Example",
                                  created_at=date.today())
        # Set on Parent Class
        da.note_id = note_id
        da.text = entity.text
        da.start = entity.start_char
        returnList.append(da)
    else:
        logging.info(f"No Entity found")

    return returnList
