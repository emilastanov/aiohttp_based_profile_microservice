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
        summary="Deletion of Education",
        description="""Method for deletion of Education""",
        parameters=[{
            'in': 'header',
            'name': 'Authorization',
            'description': 'User token.',
            'schema': {'type': 'string'},
            'required': 'true'
        }],
        responses={
            202: {
                "schema": Status,
                "description": "Status of the education deletion process."
            }
        }
    )
    @request_schema(Identifier())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension