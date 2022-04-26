from datetime import datetime

import asyncpg
from aiohttp import web

from app.middlewares.filesystem import save_file, make_dir
from app.source.data_formats import INCORRECT_REQUEST_BODY, data_created, FILE_ALREADY_EXIST
from app.source.views.files.methods.post.document import swagger_extension


__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):
        try:
            request_data = await self.request.post()

            file = request_data.get('file').file.read()
            file_name = request_data.get('title')
            user_guid = request_data.get('user_guid')
            description = request_data.get('description')

            status_mk = await make_dir(user_guid)
            status_file = await save_file(name=f"{user_guid}/{file_name}", file=file)

            if status_file == 201:
                file = await self.request.app["db"].files.create(
                    title=file_name,
                    link=f"/files?a={user_guid}x0682x{file_name}",
                    description=description,
                    created_at=datetime.now()
                )

                response = data_created({
                    "id": file.id,
                    "title": file.title,
                    "link": file.link,
                    "description": file.description,
                    "created_at": str(file.created_at),
                    "updated_at": str(file.updated_at)
                })
            else:
                response = INCORRECT_REQUEST_BODY
        except asyncpg.exceptions.UniqueViolationError:
            response = FILE_ALREADY_EXIST

        return web.json_response(**response)