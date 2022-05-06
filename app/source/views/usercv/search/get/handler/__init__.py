from aiohttp import web

from app.source.views.usercv.search.get.document import swagger_extension
from app.source.views.usercv.search.get.handler.objects import filter_cv
from app.source.views.usercv.search.get.handler.params import make_conditions

__all__ = ('Handler', )

from app.source.views.usercv.search.get.handler.response import make_cv_query_response


class Handler(web.View):

    @swagger_extension
    async def get(self):
        limit = self.request.query.get('limit') or 100
        offset = self.request.query.get('offset') or 0

        search_params = await make_conditions(self.request)
        cv_data = await filter_cv(search_params, limit, offset)

        response = await make_cv_query_response(cv_data)

        return web.json_response(**response)
