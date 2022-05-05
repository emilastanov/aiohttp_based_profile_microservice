from aiohttp import web

from app.middlewares.errors import UnknownObject, IncorrectBody
from app.source.views.driver_licenses_and_cv_link.methods import name
from app.source.views.driver_licenses_and_cv_link.methods.delete.document import swagger_extension
from app.middlewares.objects import delete_object
from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_OBJECT,
    DELETED
)

__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def delete(self):

        try:
            await delete_object(self.request, name, ['id'])
            response = DELETED

        except UnknownObject:
            response = UNKNOWN_OBJECT

        except IncorrectBody as error:
            response = INCORRECT_REQUEST_BODY
            response['data']['data']['message'] = str(error)

        return web.json_response(**response)