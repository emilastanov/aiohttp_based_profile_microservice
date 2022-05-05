from aiohttp_apispec import docs, request_schema

from app.source.views.profiles.methods import name
from app.source.views.profiles.schemas import Profiles
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Update',
        description='''Method for updating profiles.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': Profiles,
                'description': 'Data.'
            },
            404: {
                'schema': Error,
                'description': 'Profiles not found.'
            }
        }
    )
    @request_schema(Profiles())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

