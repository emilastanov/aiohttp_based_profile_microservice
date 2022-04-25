from marshmallow import Schema, fields


class Educations(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
