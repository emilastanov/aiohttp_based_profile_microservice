from app.middlewares.objects.attributes import get_object_attributes


async def make_response(model, _object, linked_table_name=None):
    attributes = get_object_attributes(model)
    response_data = {}
    if linked_table_name is None:
        for attr in attributes:
            if attributes[attr]['type'] in ('DATE', 'DATETIME', 'UUID'):
                field = getattr(_object, attr)
                response_data[attr] = str(field) if field else None
            else:
                response_data[attr] = getattr(_object, attr)
    else:
        linked_attributes = get_object_attributes(linked_table_name)
        index = 0

        for attr in attributes:
            if attributes[attr]['type'] in ('DATE', 'DATETIME', 'UUID'):
                field = _object[index]
                response_data[attr] = str(field) if field else None
            else:
                response_data[attr] = _object[index]
            index += 1

        linked_model_data = {}
        for attr in linked_attributes:
            if linked_attributes[attr]['type'] in ('DATE', 'DATETIME', 'UUID'):
                field = _object[index]
                linked_model_data[attr] = str(field) if field else None
            else:
                linked_model_data[attr] = _object[index]
            index += 1

        response_data[linked_table_name.lower()[:-1]] = linked_model_data

    return response_data
