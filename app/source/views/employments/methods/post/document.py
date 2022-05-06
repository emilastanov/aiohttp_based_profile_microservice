from aiohttp_apispec import docs, request_schema

from app.source.views.employments.methods import name
from app.source.views.employments.schemas import Employments
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Create',
        description='''Method for creating employments.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': Employments,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(Employments())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

