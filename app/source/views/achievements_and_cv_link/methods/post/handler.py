from aiohttp import web
import asyncpg.exceptions

from app.middlewares.errors import IncorrectBody
from app.middlewares.objects.response import make_response
from app.middlewares.objects import create_object
from app.source.views.achievements_and_cv_link.methods import model_name, table_name
from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    OBJECT_ALREADY_EXIST,
    data_created
)
from app.source.views.achievements_and_cv_link.methods.post.document import swagger_extension

__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):

        try:
            _object = await create_object(self.request, table_name)

            response = data_created(await make_response(model_name, _object))

        except asyncpg.exceptions.UniqueViolationError:
            response = OBJECT_ALREADY_EXIST

        except IncorrectBody as error:
            response = INCORRECT_REQUEST_BODY
            response['data']['data']['messages'] = str(error)

        return web.json_response(**response)
