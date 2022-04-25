from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.delete.document import swagger_extension
from app.source.models import *


__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def delete(self):
        response = {
            'status': web.HTTPOk.status_code,
            'data': {
                'info': 'Delete method.'
            }
        }

        return web.json_response(**response)
