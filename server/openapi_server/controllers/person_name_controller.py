import connexion
import six
import csv
import pandas as pd
import re
from flask import jsonify

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.person_name_annotation import PersonNameAnnotation  # noqa: E501
from openapi_server import util


def person_names_read_all(note=None):  # noqa: E501
    """Get all person name annotations

    Returns the person name annotations # noqa: E501

    :param note:
    :type note: list | bytes

    :rtype: List[PersonNameAnnotation]
    """
    # Get dictionary of top 1000 last names from census.gov (18-10-2020)
    # Source: https://www.census.gov/topics/population/genealogy/data/2000_surnames.html
    # TODO: Cache the data
    df = pd.read_csv("data/census_gov_top_1000_lastnames.csv")
    lastnames = df['name'].str.lower().unique().tolist()

    # TODO: Get data from https://cloud.google.com/bigquery/public-data/

    res = []
    if connexion.request.is_json:
        notes = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

        for note in notes:
            for name in lastnames:
                matches = re.finditer(name, note._text, re.IGNORECASE)
                for match in matches:
                    res.append({
                        'noteId': note._id,
                        'text':  match[0],
                        'start': match.start(),
                        'length': len(match[0])
                    })

    return jsonify(res)
