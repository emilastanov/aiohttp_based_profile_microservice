from datetime import datetime
from json import JSONDecodeError
from aiohttp import web

from app.source.views.educations.methods.patch.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


from app.source.data_formats import (
    INCORRECT_REQUEST_BODY,
    UNKNOWN_OBJECT,
    data_updated
)
from app.source.views.educations.schemas import attributes


class Handler(web.View):

    @swagger_extension
    async def patch(self):
        try:
            request_data = await self.request.json()
        except JSONDecodeError:
            request_data = None

        if request_data:
            education_id = int(request_data.get('id') or 0)
            institution = request_data.get('institution')
            type_of_education = request_data.get('v')
            degree = request_data.get('degree')
            specialization = request_data.get('specialization')
            file = request_data.get('file')
            description = request_data.get('description')
            finished_at = request_data.get('finished_at')

            education = await Educations.get(education_id)

            if education:
                new_data = {}
                if description:
                    new_data["description"] = description
                if institution:
                    new_data["institution"] = institution
                if type_of_education:
                    new_data["type_of_education"] = type_of_education
                if degree:
                    new_data["degree"] = degree
                if specialization:
                    new_data["specialization"] = specialization
                if file:
                    new_data["file"] = file
                if finished_at:
                    new_data["finished_at"] = datetime.strptime(finished_at, '%Y'),

                if new_data:
                    await education.update(**new_data).apply()

                response_data = {}
                for attr in attributes:
                    if attributes[attr]['type'] in ("DATE", "DATETIME", "UUID"):
                        response_data[attr] = str(getattr(education, attr))
                    else:
                        response_data[attr] = getattr(education, attr)
                response = data_updated(response_data)

            else:
                response = UNKNOWN_OBJECT
        else:
            response = INCORRECT_REQUEST_BODY

        return web.json_response(**response)
