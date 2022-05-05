from marshmallow import Schema, fields
from app.middlewares.objects import get_object_attributes
from app.source.views.driver_licenses_and_cv_link.methods import name


def make_attributes_of_schema():
    attributes = get_object_attributes(name)

    attr = {}
    for field in attributes:

        if attributes[field]['type'] == 'INTEGER':
            attr[field] = fields.Int()
        elif attributes[field]['type'] == 'DATETIME':
            attr[field] = fields.DateTime()
        elif attributes[field]['type'] == 'DATE':
            attr[field] = fields.Date()
        else:
            attr[field] = fields.Str()

    return attr


DriverLicensesAndCvLink = type(name, (Schema,), make_attributes_of_schema())
