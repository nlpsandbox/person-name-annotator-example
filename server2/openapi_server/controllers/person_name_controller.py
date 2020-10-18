import connexion
import six

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
    if connexion.request.is_json:
        note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
