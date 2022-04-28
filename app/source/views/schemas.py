from marshmallow import Schema, fields


def response_schema(schema, many=False):
    class Response(Schema):
        status = fields.Str()
        data = fields.Nested(schema, many=many)

    Response.__name__ = f"{schema.__name__}ResponseSchema"
    return Response


class Error(Schema):
    status = fields.Str()
    error = fields.Str()


class Identifier(Schema):
    id = fields.Int()


class Status(Schema):
    status = fields.Str()