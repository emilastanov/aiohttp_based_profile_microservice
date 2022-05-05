from json import JSONDecodeError

from aiohttp import web
import asyncpg.exceptions

from app.middlewares.objects.response import make_response
from app.middlewares.objects import create_object
from app.source.views.driverlicense.methods import name
from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    OBJECT_ALREADY_EXIST,
    data_created
)
from app.source.views.driverlicense.methods.post.document import swagger_extension

__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):

        try:
            _object = await create_object(self.request, name.lower())

            response = data_created(await make_response(name, _object))

        except asyncpg.exceptions.UniqueViolationError:
            response = OBJECT_ALREADY_EXIST

        except KeyError as error:
            response = INCORRECT_REQUEST_BODY
            response['data']['data']['message'] = str(error)

        return web.json_response(**response)
