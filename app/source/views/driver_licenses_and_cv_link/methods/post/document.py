from aiohttp_apispec import docs, request_schema

from app.source.views.driver_licenses_and_cv_link.methods import name
from app.source.views.driver_licenses_and_cv_link.schemas import DriverLicensesAndCvLink
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Create',
        description='''Method for creating driver_licenses_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': DriverLicensesAndCvLink,
                'description': 'Data.'
            },
            400: {
                'schema': Error,
                'description': 'Already exist.'
            }
        }
    )
    @request_schema(DriverLicensesAndCvLink())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

