from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.patch.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_USER_ROLE,
    data_updated
)


class Handler(web.View):

    @swagger_extension
    async def patch(self):
        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            description = request_data.get('description')
            education_id = int(request_data.get('id') or 0)
            title = request_data.get('title')
            name = request_data.get('name')

            education = await Education.get(education_id)

            if education:
                new_data = {}
                if description:
                    new_data["description"] = description
                if title:
                    new_data["title"] = title
                if name:
                    new_data["name"] = name

                if new_data:
                    await education.update(**new_data).apply()

                response = data_updated({
                    'description': education.description,
                    'title': education.title,
                    'name': education.name,
                    'id': education.id
                })
            else:
                response = UNKNOWN_USER_EDUCATION
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
