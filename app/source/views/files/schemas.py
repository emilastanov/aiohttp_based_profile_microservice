from marshmallow import Schema, fields


class Files(Schema):
    id = fields.Int()
    title = fields.Str()
    link = fields.Str()
    description = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()


