from marshmallow import Schema, fields

from app.source.models import Profiles as Model


attributes = {}
for attribute in [
                     key
                     for key in Model.__dict__.keys()
                     if '__' not in key
                 ][:-1]:
    attributes[attribute] = {
        'required': not Model
            .__dict__[attribute]
            .__dict__['column'].nullable,
        'type': str(Model
            .__dict__[attribute]
            .__dict__['column']
            .__dict__['type']).upper()
    }


def make_attributes_of_schema():
    attr = {}
    for field in attributes:

        if 'id' in field:
            attr[field] = fields.Int()
        else:
            attr[field] = fields.Str()

    return attr


Profiles = type('Profiles', (Schema,), make_attributes_of_schema())
