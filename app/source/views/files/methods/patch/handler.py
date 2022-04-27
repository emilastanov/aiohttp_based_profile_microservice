from datetime import datetime
from json import JSONDecodeError
from aiohttp import web

from app.source.data_formats import data_updated, UNKNOWN_OBJECT, INCORRECT_REQUEST_BODY
from app.source.views.files.methods.patch.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def patch(self):
        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            description = request_data.get('description')
            file_id = int(request_data.get('id') or 0)
            title = request_data.get('title')

            file = await Files.get(file_id)

            if file:
                new_data = {}
                if description:
                    new_data["description"] = description
                if title:
                    new_data["title"] = title

                if new_data:
                    new_data['updated_at'] = datetime.now()
                    await file.update(**new_data).apply()

                response = data_updated({
                    'description': file.description,
                    'title': file.title,
                    'link': file.link,
                    'updated_at': str(file.updated_at),
                    'created_at': str(file.created_at),
                    'id': file.id
                })
            else:
                response = UNKNOWN_OBJECT
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
