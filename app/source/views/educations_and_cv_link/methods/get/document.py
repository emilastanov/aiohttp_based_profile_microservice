from aiohttp_apispec import docs

from app.source.views.educations_and_cv_link.methods import name
from app.source.views.schemas import response_schema
from app.source.views.educations_and_cv_link.schemas import EduactionsAndCvLink


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Read',
        description='''Method for getting list of educations_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(EduactionsAndCvLink, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
