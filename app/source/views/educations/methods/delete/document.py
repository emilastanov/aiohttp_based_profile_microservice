from aiohttp_apispec import docs, request_schema
from marshmallow import Schema, fields

from app.source.views.schemas import (
    Status,
    Identifier
)
from app.source.views.educations.methods import name


class DeleteRequestSchema(Schema):
    id = fields.Int()


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Удаление',
        description='''Метод для удаления.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Токен пользователя.',
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
