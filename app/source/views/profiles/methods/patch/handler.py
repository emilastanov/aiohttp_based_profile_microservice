from aiohttp import web

from app.middlewares.errors import UnknownObject, IncorrectBody
from app.middlewares.objects.response import make_response
from app.source.views.profiles.methods import name
from app.source.views.profiles.methods.patch.document import swagger_extension
from app.middlewares.objects import update_object
from app.source.views.profiles.methods.post.validator import handler as validator

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
            _object = await update_object(self.request, name, validator)

            response = data_updated(await make_response(name, _object))

        except IncorrectBody as error:
            response = INCORRECT_REQUEST_BODY
            response['data']['data']['message'] = str(error)

        except UnknownObject:
            response = UNKNOWN_OBJECT

        return web.json_response(**response)
