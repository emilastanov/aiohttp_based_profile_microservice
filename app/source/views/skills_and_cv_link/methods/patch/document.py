from aiohttp_apispec import docs, request_schema

from app.source.views.skills_and_cv_link.methods import name
from app.source.views.skills_and_cv_link.schemas import SkillsAndCvLink
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Update',
        description='''Method for updating skills_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': SkillsAndCvLink,
                'description': 'Data.'
            },
            404: {
                'schema': Error,
                'description': 'SkillsAndCvLink not found.'
            }
        }
    )
    @request_schema(SkillsAndCvLink())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

