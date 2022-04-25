from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.post.document import swagger_extension
from app.source.models import *


__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):
        response = {
            'status': web.HTTPOk.status_code,
            'data': {
                'info': 'Post method.'
            }
        }

        return web.json_response(**response)
