from datetime import datetime
from json import JSONDecodeError

import asyncpg
from aiohttp import web

from app.source.data_formats import INCORRECT_REQUEST_BODY, data_created, EDUCATION_ALREADY_EXIST
from app.source.views.educations.methods.post.document import swagger_extension


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
                    institution=request_data.get('institution'),
                    type_of_education=request_data.get('type_of_education'),
                    description=request_data.get('description'),
                    degree=request_data.get('degree'),
                    specialization=request_data.get('specialization'),
                    file=request_data.get('file'),
                    finished_at=datetime.strptime(request_data.get('finished_at'), '%Y'),
                )

                response = data_created({
                    'id': educations.id,
                    'institution': educations.institution,
                    'type_of_education': educations.type_of_education,
                    'description': educations.description,
                    'degree': educations.degree,
                    'specialization': educations.degree,
                    'file': educations.file,
                    'finished_at': str(educations.finished_at),
                })

            except asyncpg.exceptions.UniqueViolationError:
                response = EDUCATION_ALREADY_EXIST
            except KeyError:
                response = INCORRECT_REQUEST_BODY
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
