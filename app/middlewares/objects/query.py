from app.middlewares.errors import UnknownObject, NoId
from app.middlewares.objects.response import make_response
from app.source import models


async def get_object_by_id(request, model_name):
    object_id = request.query.get('id')

    model = getattr(models, ''.join([word.capitalize() for word in model_name.split('_')]))

    if object_id:
        _object = await model.get(int(object_id))
    else:
        raise NoId

    if _object:
        return await make_response(model_name, _object)
    else:
        raise UnknownObject


async def get_objects(request, model_name, condition=None, linked_table_name=None):
    if condition is None:
        limit = request.query.get('limit') or 100
        offset = request.query.get('offset') or 0

    model = getattr(models, ''.join([word.capitalize() for word in model_name.split('_')]))

    data = model.__table__

    if linked_table_name:
        linked_model = getattr(models, ''.join([word.capitalize() for word in linked_table_name.split('_')]))
        data = data.join(linked_model.__table__)

    if condition is None:
        data = data.select().limit(limit).offset(offset)
    else:
        data = data.select().where(condition)

    data = await data.gino.all()
    count = await models.db.func.count(model.id).gino.scalar()

    objects = [await make_response(model_name, _object, linked_table_name=linked_table_name) for _object in data]

    return {
        "data": objects,
        "limit": limit,
        "offset": offset,
        "count": count
    } if condition is None else {
        "data": objects
    }

