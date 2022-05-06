from aiohttp_apispec import docs

from app.source.views.employments.methods import name
from app.source.views.schemas import response_schema
from app.source.views.employments.schemas import Employments


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Read',
        description='''Method for getting list of employments.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(Employments, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
