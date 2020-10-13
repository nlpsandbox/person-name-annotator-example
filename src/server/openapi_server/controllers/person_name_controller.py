import logging
import re
from datetime import date as gkdate

import connexion

from openapi_server.models.note import Note
from openapi_server.models.person_name_annotation import \
    PersonNameAnnotation  # noqa: E501


def person_names_read_all(note=None):  # noqa: E501
    """Get all person name annotations

    Returns the person name annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[PersonNameAnnotation]
    """
    person_dict = [
        'Ferdinand Houston',
        'Lindsey Cooper',
        'Juliette Ingram',
        'Elbert Hutchinson',
        'Preston Ibarra',
        'Elisabeth Mccall',
        'Moses Valentine',
        'Gilda Sheppard',
        'Marcos Wyatt',
        'Alicia Reed',
        'Matt Oconnell',
        'Ida Li',
        'Gertrude Dennis',
        'Daron Pittman',
        'Tory Carroll',
        'Wilton Andrade',
        'Nathan Crane',
        'Elizabeth Mahoney',
        'Gaston Johns',
        'Isabelle Page'
    ]
    logging.info(f"NOTE TEXT: started")
    found = False
    counter = 1
    return_list = []
    if connexion.request.is_json:
        found = True
        note = [Note.from_dict(d) for d in
                connexion.request.get_json()]  # noqa: E501
        note_text = note[0]._text
        note_id = note[0]._id
        logging.info(f"NOTE TEXT: {note_text}")

        for name in person_dict:
            match = f"{name}"
            match = re.finditer(
                match,
                note[0]._text)
            add_match(counter, match, note, return_list)

        for m in return_list:
            logging.info(f" text set to : {m.text}")

    return return_list


def add_match(counter, match, note, returnList):
    if match is not None:
        for m in match:
            logging.info(f"Date : {m[0]} found at {m.start()}")
            da = PersonNameAnnotation(id=counter,
                                      created_by="Person Date Annotation "
                                                 "Example",
                                      created_at=gkdate.today(),
                                      )
            da.text = m[0]
            da.note_id = note[0].id
            da.start = m.start()
            returnList.append(da)
    else:
        logging.warn(f"No Person found")
