from marshmallow import Schema, fields

from app.source.views.schemas import response_schema


class EducationListSchema(Schema):
    id = fields.Int()
    institution = fields.Str()
    type_of_education = fields.Str()
    degree = fields.Str()
    specialization = fields.Str()
    file = fields.Str()
    description = fields.Str()
    finished_at = fields.Str()


education_list_schema_response = response_schema(EducationListSchema, many=True)