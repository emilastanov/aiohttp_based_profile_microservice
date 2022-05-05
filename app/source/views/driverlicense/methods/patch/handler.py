from aiohttp import web

from app.middlewares.errors import UnknownObject
from app.middlewares.objects.response import make_response
from app.middlewares.objects import update_object
from app.source.views.driverlicense.methods import name
from app.source.views.driverlicense.methods.patch.document import swagger_extension

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
            _object = await update_object(self.request, name)

            response = data_updated(await make_response(name, _object))

        except KeyError:
            response = INCORRECT_REQUEST_BODY

        except UnknownObject:
            response = UNKNOWN_OBJECT

        return web.json_response(**response)
