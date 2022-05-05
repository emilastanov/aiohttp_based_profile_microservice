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


async def get_objects(request, model_name, condition=None):
    if condition is None:
        limit = request.query.get('limit') or 100
        offset = request.query.get('offset') or 0

    model = getattr(models, ''.join([word.capitalize() for word in model_name.split('_')]))

    data = model.__table__.select()
    if condition is None:
        data = await data.limit(limit).offset(offset).gino.all()
    else:
        data = await data.where(condition).gino.all()

    count = await models.db.func.count(model.id).gino.scalar()

    objects = [await make_response(model_name, _object) for _object in data]

    return {
        "data": objects,
        "limit": limit,
        "offset": offset,
        "count": count
    } if condition is None else {
        "data": objects
    }

