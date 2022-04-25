from json import JSONDecodeError
from aiohttp import web

from app.source.views.profiles.methods.patch.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def patch(self):
        response = {
            'status': web.HTTPOk.status_code,
            'data': {
                'info': 'Patch method.'
            }
        }

        return web.json_response(**response)
