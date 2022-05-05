from aiohttp_apispec import docs

from app.source.views.achievements_and_cv_link.methods import model_name
from app.source.views.schemas import response_schema
from app.source.views.achievements_and_cv_link.schemas import AchievementsAndCVLink


def swagger_extension(method):
    @docs(
        tags=[model_name],
        summary='Read',
        description='''Method for getting list of.achievements_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(AchievementsAndCVLink, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
