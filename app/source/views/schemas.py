from marshmallow import Schema, fields


class Error(Schema):
    status = fields.Str()
    error = fields.Str()


class Identifier(Schema):
    id = fields.Int()


class Status(Schema):
    status = fields.Str()


def response_schema(schema, many=False):
    class Response(Schema):
        status = fields.Str()
        data = fields.Nested(schema, many=many)

    Response.__name__ = f'{"".join([word.capitalize() for word in schema.__name__.split("_")])}ResponseSchema'
    return Response

