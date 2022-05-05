from aiohttp_apispec import docs, request_schema

from app.source.views.educations_and_cv_link.methods import name
from app.source.views.educations_and_cv_link.schemas import EduactionsAndCvLink
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Create',
        description='''Method for creating educations_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': EduactionsAndCvLink,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(EduactionsAndCvLink())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

