from aiohttp_apispec import docs, request_schema

from app.source.views.educations.methods import name
from app.source.views.educations.schemas import Educations
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary="Updating the type of education",
        description="Method for updating education",
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'User token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                # 'schema': {},
                'description': ""
            },
            400: {
                'schema': Error,
                'description': ""
            }
        }
    )
    @request_schema(Educations())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

