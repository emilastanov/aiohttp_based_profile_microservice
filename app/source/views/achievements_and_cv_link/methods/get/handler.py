from aiohttp import web

from app.middlewares.objects import get_object_by_id, get_objects
from app.middlewares.errors import UnknownObject, NoId
from app.source.data_formats import query_data, UNKNOWN_OBJECT
from app.source.views.achievements_and_cv_link.methods.get.document import swagger_extension
from app.source.views.achievements_and_cv_link.methods import model_name

__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):

        try:
            _object = await get_object_by_id(self.request, model_name)
            response = query_data(_object)

        except UnknownObject:
            response = UNKNOWN_OBJECT

        except NoId:
            objects = await get_objects(self.request, model_name)
            response = query_data(**objects)

        return web.json_response(**response)