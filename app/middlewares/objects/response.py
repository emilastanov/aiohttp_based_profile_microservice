from app.middlewares.objects.attributes import get_object_attributes


async def make_response(model, _object):
    attributes = get_object_attributes(model)
    response_data = {}
    for attr in attributes:
        if attributes[attr]['type'] in ('DATE', 'DATETIME', 'UUID'):
            response_data[attr] = str(getattr(_object, attr))
        else:
            response_data[attr] = getattr(_object, attr)
    return response_data
