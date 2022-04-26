from marshmallow import Schema, fields


class Files(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
