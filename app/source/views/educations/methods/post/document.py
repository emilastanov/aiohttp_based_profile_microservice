from aiohttp_apispec import docs, request_schema

from app.source.views.educations.methods import name
from app.source.views.educations.schemas import Educations
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Создание',
        description='''Метод создания.''',
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
                'description': 'Данные.'
            },
            400: {
                'schema': Error,
                'description': 'Уже существует.'
            }
        }
    )
    @request_schema(Educations())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

