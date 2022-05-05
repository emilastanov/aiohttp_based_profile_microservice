from aiohttp_apispec import docs

from app.source.views.driver_licenses_and_cv_link.methods import name
from app.source.views.schemas import response_schema
from app.source.views.driver_licenses_and_cv_link.schemas import DriverLicensesAndCvLink


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Read',
        description='''Method for getting list of driver_licenses_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': response_schema(DriverLicensesAndCvLink, many=True),
                'description': 'List.'
            }
        }
    )
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension
