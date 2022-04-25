from marshmallow import Schema, fields


class Error(Schema):
    status = fields.Str()
    error = fields.Str()


class Identifier(Schema):
    id = fields.Int()


class Status(Schema):
    status = fields.Str()
