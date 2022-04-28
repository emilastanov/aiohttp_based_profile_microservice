from datetime import datetime
from json import JSONDecodeError

from aiohttp import web
import asyncpg.exceptions

from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    OBJECT_ALREADY_EXIST,
    data_created
)
from app.source.views.profiles.methods.post.document import swagger_extension
from app.source.views.profiles.schemas import attributes

__all__ = ('Handler',)


class Handler(web.View):

    @swagger_extension
    async def post(self):

        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            try:
                _object = await self.request.app['db'].profiles.create(
                    last_name=request_data['last_name'],
                    first_name=request_data['first_name'],
                    middle_name=request_data['middle_name'],
                    registered_at=datetime.now(),
                    location=request_data['location'],
                    available_for_offers=request_data.get('available_for_offers'),
                    date_of_birthday=datetime.strptime(
                        request_data.get('date_of_birthday'), '%Y-%m-%d'
                    ) if request_data.get('date_of_birthday') else None,
                    sex=request_data.get('sex'),
                    guid=request_data['guid']
                )

                response_data = {}
                for attr in attributes:
                    if attributes[attr]['type'] in ("DATE", "DATETIME", "UUID"):
                        response_data[attr] = str(getattr(_object, attr))
                    else:
                        response_data[attr] = getattr(_object, attr)

                response = data_created(response_data)

            except asyncpg.exceptions.UniqueViolationError:
                response = OBJECT_ALREADY_EXIST
            except KeyError:
                response = INCORRECT_REQUEST_BODY
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
