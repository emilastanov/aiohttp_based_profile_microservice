from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.get.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):

        data = await Education.query.gino.all()

        roles = [{
            "description": education.description,
            "title": education.title,
            "name": education.name,
            "id": education.id,
        } for education in data]

        response = query_data(educations)

        return web.json_response(**response)