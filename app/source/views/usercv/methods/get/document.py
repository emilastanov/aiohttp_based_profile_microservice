from aiohttp_apispec import docs

from app.source.views.usercv.methods import model_name
from app.source.views.schemas import response_schema
from app.source.views.usercv.schemas import UserCv as Schema

UserCv = response_schema(Schema, many=True)


def swagger_extension(method):
    @docs(
        tags=[model_name],
        summary='Read',
        description='''Method for getting list of usercv.''',
        parameters=[{
            'in': 'query',
            'name': 'id',
            'description': 'Object id.',
            'schema': {'type': 'string'},
        }, {
            'in': 'query',
            'name': 'limit',
            'description': 'Limit of object in response.',
            'schema': {'type': 'string'},
        }, {
            'in': 'query',
            'name': 'offset',
            'description': 'Offset of object in response.',
            'schema': {'type': 'string'},
        }],
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
