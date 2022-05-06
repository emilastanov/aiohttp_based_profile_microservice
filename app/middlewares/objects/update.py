from asyncpg import ForeignKeyViolationError

from app.middlewares.models import get_model_by_name
from app.middlewares.objects.attributes import get_object_attributes
from app.middlewares.objects.request import get_request_json_body
from app.middlewares.errors import UnknownObject


async def handler(request, model, validator=lambda res: res):
    attributes = get_object_attributes(model)

    request_data = validator(
        await get_request_json_body(
            request,
            attributes,
            get_object_id=True,
            use_require_fields=False
        )
    )

    update_data = {}
    for field in request_data:
        if request_data[field]:
            update_data[field] = request_data[field]

    _object = await get_model_by_name(model).get(update_data.pop('id'))

    try:
        if _object and update_data:
            await _object.update(**update_data).apply()
        elif not _object:
            raise UnknownObject
    except ForeignKeyViolationError:
        raise UnknownObject

    return _object

