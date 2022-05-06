from aiohttp import web

from app.middlewares.objects import get_object_by_id, get_objects
from app.source.data_formats import query_data
from app.source.views.usercv.search.get.document import swagger_extension
from app.source.views.usercv.methods import table_name
from app.source.views.usercv.search.get.handler.objects import filter_by_linked_models_param
from app.source.views.usercv.search.get.handler.params import make_conditions

__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):
        # _object = await get_object_by_id(self.request, table_name)
        # response = query_data(_object)
        search_params = await make_conditions(self.request)
        print(await filter_by_linked_models_param('skills_and_cv_link', search_params['skills']))

        return web.json_response(data=str(search_params))
