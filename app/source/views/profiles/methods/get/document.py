from aiohttp_apispec import docs

from app.source.views.profiles.methods import name
from app.source.views.schemas import response_schema
from app.source.views.profiles.schemas import Profiles


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Read',
        description='''Method for getting list of profiles.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(Profiles, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
