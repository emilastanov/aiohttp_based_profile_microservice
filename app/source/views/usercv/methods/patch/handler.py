from aiohttp import web

from app.middlewares.errors import UnknownObject, IncorrectBody
from app.middlewares.objects.response import make_response
from app.source.views.usercv.methods import model_name, table_name
from app.source.views.usercv.methods.patch.document import swagger_extension
from app.middlewares.objects import update_object

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
            _object = await update_object(self.request, table_name)

            response = data_updated(await make_response(model_name, _object))

        except IncorrectBody:
            response = INCORRECT_REQUEST_BODY

        except UnknownObject:
            response = UNKNOWN_OBJECT

        return web.json_response(**response)
