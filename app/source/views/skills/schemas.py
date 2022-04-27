from marshmallow import Schema, fields

from app.source.models import Skills as Model


attributes = [
                 key
                 for key in Model.__dict__.keys()
                 if '__' not in key
             ][:-1]


def make_attributes_of_schema():
    attr = {}
    for field in attributes:

        if 'id' in field:
            attr[field] = fields.Int()
        else:
            attr[field] = fields.Str()

    return attr


Skills = type('Skills', (Schema,), make_attributes_of_schema())
