from aiohttp_apispec import docs, request_schema

from app.source.views.hobbies.methods import name
from app.source.views.hobbies.schemas import Hobbies
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Create',
        description='''Method for creating hobbies.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': Hobbies,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(Hobbies())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

