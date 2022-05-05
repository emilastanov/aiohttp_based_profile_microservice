from marshmallow import Schema, fields
from app.middlewares.objects import get_object_attributes
from app.source.views.achievements_and_cv_link.methods import table_name


def make_attributes_of_schema():
    attributes = get_object_attributes(table_name)

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


AchievementsAndCVLink = type(table_name, (Schema,), make_attributes_of_schema())
