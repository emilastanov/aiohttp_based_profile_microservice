from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.post.document import swagger_extension
from app.source.models import *


__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):

        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            try:
                educations = await self.request.app["db"].educations.create(
                    institution=request_data['institution'],
                    type_of_education=request_data['type_of_education'],
                    description=request_data['description'],
                    degree=request_data['degree'],
                    specialization=request_data['specialization'],
                    file=request_data['file'],
                    finished_at=request_data['finished_at'],
                )

                response = data_created({
                    'id': educations.id,
                    'institution': educations.institution,
                    'type_of_education': educations.type_of_education,
                    'description': educations.description,
                    'degree': educations.degree,
                    'specialization': educations.degree,
                    'file': educations.file,
                    'finished_at': educations.finished_at,
                })

            except asyncpg.exceptions.UniqueViolationError:
                response = education_ALREADY_EXIST
            except KeyError:
                response = INCORRECT_REQUEST_BODY
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
