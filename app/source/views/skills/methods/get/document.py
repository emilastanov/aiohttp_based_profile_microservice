from aiohttp_apispec import docs

from app.source.views.skills.methods import name
from app.source.views.schemas import response_schema
from app.source.views.skills.schemas import Skills


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Read',
        description='''Method for getting list of skills.''',
        parameters=[{
            'in': 'query',
            'name': 'id',
            'description': 'Object id.',
            'schema': {'type': 'string'},
        }, {
            'in': 'query',
            'name': 'limit',
            'description': 'Limit of object in response.',
            'schema': {'type': 'string'},
        }, {
            'in': 'query',
            'name': 'offset',
            'description': 'Offset of object in response.',
            'schema': {'type': 'string'},
        }],
        responses={
            200: {
                'schema': response_schema(Skills, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
