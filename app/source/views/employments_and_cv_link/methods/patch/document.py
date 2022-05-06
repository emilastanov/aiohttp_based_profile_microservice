from aiohttp_apispec import docs, request_schema

from app.source.views.employments_and_cv_link.methods import name
from app.source.views.employments_and_cv_link.schemas import EmploymentsAndCvLink
from app.source.views.schemas import Error


def swagger_extension(method):
    @docs(
        tags=[name],
        summary='Update',
        description='''Method for updating employments_and_cv_link.''',
        # parameters=[{
        #     'in': 'header',
        #     'name': 'Authorization',
        #     'description': 'Access token.',
        #     'schema': {'type': 'string'},
        #     'required': 'true'
        # }],
        responses={
            200: {
                'schema': EmploymentsAndCvLink,
                'description': 'Data.'
            },
            404: {
                'schema': Error,
                'description': 'EmploymentsAndCvLink not found.'
            }
        }
    )
    @request_schema(EmploymentsAndCvLink())
    def extension(*args, **kwargs):
        return method(*args, **kwargs)

    return extension

