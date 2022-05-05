from asyncpg import DataError

from app.middlewares.errors import UnknownObject, IncorrectBody
from app.middlewares.objects.request import get_request_json_body
from app.source import models


async def handler(request, model, attributes):
    request_data = await get_request_json_body(request, attributes, get_object_id=True, use_require_fields=False)
    model = getattr(models, model)

    try:
        _object = await model.get(request_data['id'])
    except DataError as error:
        raise IncorrectBody(error)

    if _object:
        return await _object.delete()
    else:
        raise UnknownObject
