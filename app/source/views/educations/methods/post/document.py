from aiohttp_apispec import docs, request_schema

from app.source.views.educations.methods import name
from app.source.views.educations.schemas import Educations
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary="Creating of Education",
        description="""Creation method Education. Data validation is not provided.""",
        responses={
            200: {
                "schema": Educations,
                "description": "Education data."
            },
            400: {
                "schema": Error,
                "description": "Education is already exist."
            }
        }
    )
    @request_schema(Educations())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

