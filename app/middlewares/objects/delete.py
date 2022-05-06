from asyncpg import DataError

from app.middlewares.errors import UnknownObject, IncorrectBody
from app.middlewares.models import get_model_by_name
from app.middlewares.objects.request import get_request_json_body


async def handler(request, model, attributes):
    request_data = await get_request_json_body(request, attributes, get_object_id=True, use_require_fields=False)
    model = get_model_by_name(model)

    try:
        _object = await model.get(request_data['id'])
    except DataError as error:
        raise IncorrectBody(error)

    if _object:
        return await _object.delete()
    else:
        raise UnknownObject
