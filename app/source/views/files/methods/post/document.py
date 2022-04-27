from aiohttp_apispec import docs, request_schema

from app.source.views.files.methods import name
from app.source.views.files.schemas import Files
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Загрузка файла',
        description='''Метод создания.''',
        parameters=[{
            'in': 'formData',
            'name': 'file',
            'description': 'Файл.',
            'type': 'file',
            'required': 'true'
        }, {
            'in': 'formData',
            'name': 'title',
            'description': 'Название файла.',
            'type': 'string',
            'required': 'true'
        }, {
            'in': 'formData',
            'name': 'user_guid',
            'description': 'GUID пользователя.',
            'type': 'string',
            'required': 'true'
        }, {
            'in': 'formData',
            'name': 'description',
            'description': 'Описание файла.',
            'type': 'string',
        }],
        responses={
            200: {
                'schema': Files,
                'description': 'Данные.'
            },
            400: {
                'schema': Error,
                'description': 'Уже существует.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

