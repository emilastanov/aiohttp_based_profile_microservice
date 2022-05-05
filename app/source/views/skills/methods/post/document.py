from aiohttp_apispec import docs, request_schema

from app.source.views.skills.methods import name
from app.source.views.skills.schemas import Skills
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Create',
        description='''Method for creating skills.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': Skills,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(Skills())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

