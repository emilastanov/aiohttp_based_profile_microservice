from aiohttp_apispec import docs, request_schema

from app.source.views.skills.methods import name
from app.source.views.skills.schemas import Skills
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Update',
        description='''Method for updating skills.''',
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
            404: {
                'schema': Error,
                'description': 'Skills not found.'
            }
        }
    )
    @request_schema(Skills())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

