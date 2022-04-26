from json import JSONDecodeError
from aiohttp import web

from app.middlewares.filesystem import delete_file
from app.source.data_formats import DELETED, INCORRECT_REQUEST_BODY, UNKNOWN_FILE
from app.source.views.files.methods.delete.document import swagger_extension
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
            file_id = int(request_data.get('id') or 0)

            file = await Files.get(file_id)
            if file:
                await file.delete()

                file_name = '/'.join(file.link.split('=')[-1].split('x0682x'))
                status = await delete_file(file_name)

                if status == status:
                    response = DELETED
                else:
                    response = UNKNOWN_FILE
            else:
                response = UNKNOWN_FILE
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
