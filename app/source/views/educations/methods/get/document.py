from aiohttp_apispec import docs

from app.source.views.educations.methods import name
from app.source.views.schemas import response_schema
from app.source.views.educations.schemas import Educations


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary="List of Education",
        description="""Method for getting a list of educations.""",
        responses={
            200: {
                "schema": response_schema(Educations, many=True),
                "description": "A list of educations."
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
