import connexion
import pandas as pd
import re

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.text_person_name_annotations import TextPersonNameAnnotations  # noqa: E501

# Get dictionary of top 1000 last names from census.gov (18-10-2020)
# https://www.census.gov/topics/population/genealogy/data/2000_surnames.html
lastnames_df = pd.read_csv("data/census_gov_top_1000_lastnames.csv")
lastnames = lastnames_df['name'].str.lower().unique().tolist()


def create_text_person_name_annotations(note=None):  # noqa: E501
    """Annotate person names in a clinical note

    Return the person name annotations found in a clinical note # noqa: E501

    :param note:
    :type note: dict | bytes

    :rtype: TextPersonNameAnnotations
    """
    res = None
    status = None

    if connexion.request.is_json:
        try:
            note = Note.from_dict(connexion.request.get_json())  # noqa: E501

            annotations = []
            for name in lastnames:
                matches = re.finditer(name, note._text, re.IGNORECASE)
                for match in matches:
                    annotations.append({
                        'start': match.start(),
                        'length': len(match[0]),
                        'text':  match[0]
                    })

            res = TextPersonNameAnnotations(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status
