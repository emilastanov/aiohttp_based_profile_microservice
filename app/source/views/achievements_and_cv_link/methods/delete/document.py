from aiohttp_apispec import docs, request_schema
from marshmallow import Schema, fields

from app.source.views.schemas import (
    Status,
    Identifier
)
from app.source.views.achievements_and_cv_link.methods import model_name


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in model_name.split('_')])],
        summary='Delete',
        description='''Method for deleting.achievements_and_cv_link.''',
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
