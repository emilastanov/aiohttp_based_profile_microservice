from json import JSONDecodeError

from aiohttp import web
import asyncpg.exceptions

from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    OBJECT_ALREADY_EXIST,
    data_created
)
from app.source.views.skills.methods.post.document import swagger_extension


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
                _object = await self.request.app['db'].skills.create(
                    meta_title=request_data['meta_title'],
                    title=request_data['title'],
                    course_id=request_data.get('course_id')
                )

                response = data_created({
                    'id': _object.id,
                    'meta_title': _object.meta_title,
                    'title': _object.title,
                    'course_id': _object.course_id,
                })

            except asyncpg.exceptions.UniqueViolationError:
                response = OBJECT_ALREADY_EXIST
            except KeyError:
                response = INCORRECT_REQUEST_BODY
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
