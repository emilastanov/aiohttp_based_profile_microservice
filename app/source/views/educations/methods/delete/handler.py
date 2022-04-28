from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.delete.document import swagger_extension
from app.source.models import *


__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def delete(self):

        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            education_id = int(request_data.get('id') or 0)

            education = await Education.get(education_id)
            if education:
                await education.delete()

                response = DELETED
            else:
                response = UNKNOWN_USER_EDUCATION
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)