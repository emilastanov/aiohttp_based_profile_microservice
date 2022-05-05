from aiohttp_apispec import docs, request_schema

from app.source.views.usercv.methods import model_name
from app.source.views.usercv.schemas import UserCv
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[model_name],
        summary='Create',
        description='''Method for creating usercv.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': UserCv,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(UserCv())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

