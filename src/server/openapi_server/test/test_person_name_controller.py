# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.person_name_annotation import PersonNameAnnotation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPersonNameController(BaseTestCase):
    """PersonNameController integration test stubs"""

    def test_person_names_read_all(self):
        """Test case for person_names_read_all

        Get all person name annotations
        """
        note = {
            "filename": "260-01.xml",
            "text": "October 3, Ms Chloe Price met with...",
            "type": "pathology",
            "patientPublicId": ""
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/person-names',
            method='GET',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
