from aiohttp_apispec import docs

from app.source.views.usercv.methods import model_name
from app.source.views.schemas import response_schema
from app.source.views.usercv.schemas import UserCv


def swagger_extension(method):
    @docs(
        tags=[model_name],
        summary='Read',
        description='''Method for getting list of usercv.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(UserCv, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
