from datetime import datetime
from json import JSONDecodeError
from aiohttp import web

from app.source.views.profiles.methods.patch.document import swagger_extension
from app.source.models import *

__all__ = ('Handler', )


from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_OBJECT,
    data_updated
)
from app.source.views.profiles.schemas import attributes


class Handler(web.View):

    @swagger_extension
    async def patch(self):
        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:

            object_id = int(request_data.get('id') or 0)
            last_name = request_data.get('last_name')
            first_name = request_data.get('first_name')
            middle_name = request_data.get('middle_name')
            location = request_data.get('location')
            available_for_offers = request_data.get('available_for_offers')
            date_of_birthday = request_data.get('date_of_birthday')
            sex = request_data.get('sex')

            _object = await Profiles.get(object_id)

            if _object:
                new_data = {}
                if last_name:
                    new_data['last_name'] = last_name
                if first_name:
                    new_data['first_name'] = first_name
                if middle_name:
                    new_data['middle_name'] = middle_name
                if location:
                    new_data['location'] = location
                if available_for_offers:
                    new_data['available_for_offers'] = available_for_offers
                if date_of_birthday:
                    new_data['date_of_birthday'] = datetime.strptime(
                        date_of_birthday, '%Y-%m-%d'
                    )
                if sex:
                    new_data['sex'] = sex

                if new_data:
                    await _object.update(**new_data).apply()

                response_data = {}
                for attr in attributes:
                    if attributes[attr]['type'] in ("DATE", "DATETIME", "UUID"):
                        response_data[attr] = str(getattr(_object, attr))
                    else:
                        response_data[attr] = getattr(_object, attr)

                response = data_updated(response_data)
            else:
                response = UNKNOWN_OBJECT
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
