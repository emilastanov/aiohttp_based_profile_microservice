from aiohttp_apispec import docs

from app.source.views.usercv.methods import table_name
from app.source.views.usercv.methods.get.document import UserCv


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in table_name.split('_')])],
        summary='Read',
        description='''Method for searching cv.''',
        deprecated=True,
        parameters=[{
            'in': 'query',
            'name': 'id',
            'description': 'Object identity number.',
        }],
        responses={
            200: {
                'schema': UserCv,
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
