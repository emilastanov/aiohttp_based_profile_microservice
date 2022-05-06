from aiohttp_apispec import docs

from app.source.views.usercv.methods import table_name
from app.source.views.usercv.methods.get.document import UserCv


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in table_name.split('_')])],
        summary='Read',
        description='''Method for searching cv.''',
        # deprecated=True,
        parameters=[{
            'in': 'query',
            'name': 'skills',
            'description': 'Array of skills.',
        }, {
            'in': 'query',
            'name': 'achievements',
            'description': 'Array of achievements.',
        }, {
            'in': 'query',
            'name': 'educations',
            'description': 'Array of educations.',
        }, {
            'in': 'query',
            'name': 'employments',
            'description': 'Array of employments.',
        }, {
            'in': 'query',
            'name': 'hobbies',
            'description': 'Array of hobbies.',
        }, {
            'in': 'query',
            'name': 'driver_licenses',
            'description': 'Array of driver licenses.',
        }, {
            'in': 'query',
            'name': 'max_salary',
            'description': 'Max salary.',
        }, {
            'in': 'query',
            'name': 'min_salary',
            'description': 'Min salary.',
        }, {
            'in': 'query',
            'name': 'wish_position',
            'description': 'Wish position.',
        }, {
            'in': 'query',
            'name': 'possibility_of_moving',
            'description': 'Possibility of moving.',
        }, {
            'in': 'query',
            'name': 'work_format',
            'description': 'Work format.',
        }, {
            'in': 'query',
            'name': 'marital_status',
            'description': 'Marital status.',
        }, {
            'in': 'query',
            'name': 'limit',
            'description': 'Limit of rows.',
        }, {
            'in': 'query',
            'name': 'offset',
            'description': 'Offset of rows.',
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
