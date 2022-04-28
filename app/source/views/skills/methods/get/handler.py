from aiohttp import web

from app.source.views.skills.methods.get.document import swagger_extension
from app.source.data_formats import query_data
from app.source.models import *
from app.source.views.skills.schemas import attributes


__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):

        object_id = self.request.query.get('id') or 0
        limit = self.request.query.get('limit') or 100
        offset = self.request.query.get('offset') or 0

        if object_id:
            data = [await Skills.get(int(object_id))]
            count = 1
        else:
            data = await Skills.__table__.select().limit(limit).offset(offset).gino.all()
            count = await db.func.count(Skills.id).gino.scalar()

        objects = []

        for _object in data:
            res = {}
            for attr in attributes:
                res[attr] = getattr(_object, attr)
            objects.append(res)

        if object_id:
            response = query_data(
                objects[0]
            )
        else:
            response = query_data(
                objects,
                limit=limit,
                offset=offset,
                count=count
            )

        return web.json_response(**response)
