from aiohttp import web

from app.middlewares.filesystem import get_file
from app.source.data_formats import query_data
from app.source.views.files.methods.get.document import swagger_extension
from app.source.models import *


__all__ = ('Handler', )


class Handler(web.View):

    @swagger_extension
    async def get(self):
        if self.request.query.get('a'):
            file = self.request.query.get('a').split('x0682x')
            guid = file[0]
            name = file[1]

            file, status, headers = await get_file(f'{guid}/{name}')
            content_type = headers.get('Content-Type')
            return web.Response(body=file, status=status, headers={'Content-Type': content_type})
        else:
            limit = self.request.query.get('limit') or 100
            offset = self.request.query.get('offset') or 0

            data = await Files.__table__.select().limit(limit).offset(offset).gino.all()
            count = await db.func.count(Files.id).gino.scalar()

            response = query_data([
                {
                    'id': obj[0],
                    "title": obj[1],
                    "link": obj[2],
                    "description": obj[5],
                    "created_at": str(obj[3]),
                    "updated_at": str(obj[4])
                } for obj in data
            ],
                limit=limit,
                offset=offset,
                count=count
            )

            return web.json_response(**response)
