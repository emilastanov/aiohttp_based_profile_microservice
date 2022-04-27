from json import JSONDecodeError
from aiohttp import web

from app.source.views.skills.methods.patch.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )

from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_OBJECT,
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
            meta_title = request_data.get('meta_title')
            object_id = int(request_data.get('id') or 0)
            title = request_data.get('title')
            course_id = request_data.get('course_id')

            _object = await Skills.get(object_id)

            if _object:
                new_data = {}
                if meta_title:
                    new_data['meta_title'] = meta_title
                if title:
                    new_data['title'] = title
                if course_id:
                    new_data['course_id'] = course_id

                if new_data:
                    await _object.update(**new_data).apply()

                response = data_updated({
                    'meta_title': _object.meta_title,
                    'title': _object.title,
                    'course_id': _object.course_id,
                    'id': _object.id
                })
            else:
                response = UNKNOWN_OBJECT
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
