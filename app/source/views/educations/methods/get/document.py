from aiohttp_apispec import docs

from app.source.views.educations.methods import name


def swagger_extension(method):
    @docs(
        tags=[name],
        summary="",
        description="",
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Токен пользователя.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                # 'schema': {},
                'description': ""
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
