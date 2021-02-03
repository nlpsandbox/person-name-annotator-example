from openapi_server.models.service import Service  # noqa: E501
from openapi_server.models.license import License


def service():  # noqa: E501
    """Get service information

    Get information about the service # noqa: E501


    :rtype: Service
    """
    service = Service(
        name="person-name-annotator-example",
        version="0.2.3",
        license=License.APACHE_2_0,
        repository="github:nlpsandbox/person-name-annotator-example",
        description="An example implementation of the NLP Sandbox " +
                    "Person Name Annotator API",
        author="The NLP Sandbox Team",
        author_email="thomas.schaffter@sagebionetworks.org",
        url="https://github.com/nlpsandbox/person-name-annotator-example"
    )
    return service, 200
