from json import JSONDecodeError
from aiohttp import web

from app.source.views.skills.methods.delete.document import swagger_extension
from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_OBJECT,
    DELETED
)
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
            object_id = int(request_data.get('id') or 0)

            _object = await Skills.get(object_id)
            if _object:
                await _object.delete()

                response = DELETED
            else:
                response = UNKNOWN_OBJECT
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
