from aiohttp_apispec import docs, request_schema

from app.source.views.achievements_and_cv_link.methods import model_name
from app.source.views.achievements_and_cv_link.schemas import AchievementsAndCVLink
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[model_name],
        summary='Create',
        description='''Method for creating.achievements_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': AchievementsAndCVLink,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(AchievementsAndCVLink())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

