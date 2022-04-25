from marshmallow import Schema, fields


class Profiles(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
