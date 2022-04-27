from aiohttp_apispec import docs

from app.source.views.files.methods import name
from app.source.views.files.schemas import Files


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Список файлов | Скачивание файла',
        description='''Метод для получения списка.''',
        parameters=[{
            'in': 'query',
            'name': 'a',
            'description': 'Адрес файла.',
            'schema': {'type': 'string'},
        }, {
            'in': 'query',
            'name': 'limit',
            'description': 'Адрес файла.',
            'schema': {'type': 'integer'},
        }, {
            'in': 'query',
            'name': 'offset',
            'description': 'Адрес файла.',
            'schema': {'type': 'integer'},
        }],
        responses={
            200: {
                'schema': Files,
                'description': 'Список.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
