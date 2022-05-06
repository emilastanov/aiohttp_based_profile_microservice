from aiohttp_apispec import docs, request_schema

from app.source.views.employments.methods import name
from app.source.views.employments.schemas import Employments
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Update',
        description='''Method for updating employments.''',
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
            404: {
                'schema': Error,
                'description': 'Employments not found.'
            }
        }
    )
    @request_schema(Employments())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

