from aiohttp_apispec import docs

from app.source.views.educations.schemas import education_list_schema_response
from app.source.views.educations.methods import name


def swagger_extension(method):
    @docs(
        tags=[name],
        summary="List of Education",
        description="""Method for getting a list of educations.""",
        parameters=[{
            'in': 'header',
            'name': 'Authorization',
            'description': 'User token.',
            'schema': {'type': 'string'},
            'required': 'true'
        }],
        responses={
            200: {
                "schema": education_list_schema_response,
                "description": "A list of educations."
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
