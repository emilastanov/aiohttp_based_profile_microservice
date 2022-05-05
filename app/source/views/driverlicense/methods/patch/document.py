from aiohttp_apispec import docs, request_schema

from app.source.views.driverlicense.methods import name
from app.source.views.driverlicense.schemas import DriverLicense
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[''.join([word.capitalize() for word in name.split('_')])],
        summary='Update',
        description='''Method for updating driverlicense.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': DriverLicense,
                'description': 'Data.'
            },
            404: {
                'schema': Error,
                'description': 'DriverLicense not found.'
            }
        }
    )
    @request_schema(DriverLicense())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

