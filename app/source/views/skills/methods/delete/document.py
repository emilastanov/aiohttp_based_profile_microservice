from aiohttp_apispec import docs, request_schema
from marshmallow import Schema, fields

from app.source.views.schemas import (
    Status,
    Identifier
)
from app.source.views.skills.methods import name


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Delete',
        description='''Method for deleting skills.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            202: {
                'schema': Status,
                'description': 'Статус процесса удаления.'
            }
        }
    )
    @request_schema(Identifier())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
