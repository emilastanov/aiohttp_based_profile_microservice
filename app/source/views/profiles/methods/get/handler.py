from aiohttp import web

from app.source.views.profiles.methods.get.document import swagger_extension
from app.source.data_formats import query_data
from app.source.models import *
from app.source.views.profiles.schemas import attributes

__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):

        object_id = self.request.query.get('id')

        data = [
            await Profiles.get(int(object_id))
        ] if object_id else \
            await Profiles.query.gino.all()

        objects = []

        for _object in data:
            res = {}
            for attr in attributes:
                if attributes[attr]['type'] in ("DATE", "DATETIME", "UUID"):
                    res[attr] = str(getattr(_object, attr))
                else:
                    res[attr] = getattr(_object, attr)
            objects.append(res)

        response = query_data(
            objects[0]
            if object_id else
            objects
        )

        return web.json_response(**response)
