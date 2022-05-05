from aiohttp_apispec import docs, request_schema

from app.source.views.files.methods import name
from app.source.views.files.schemas import Files
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Изменение данных файла',
        description='''Метод изменения данных файла.''',
        responses={
            200: {
                'schema': Files,
                'description': 'Данные файла.'
            },
            400: {
                'schema': Error,
                'description': 'Файл уже существует.'
            }
        }
    )
    @request_schema(Files())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

