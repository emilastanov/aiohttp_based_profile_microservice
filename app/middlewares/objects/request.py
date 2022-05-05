from json import JSONDecodeError

from app.middlewares.errors import IncorrectBody


async def get_request_json_body(request, attributes, get_object_id=False, use_require_fields=True):
    try:
        request_data = await request.json()

        object_data = {}
        for attr in attributes:
            if attr == 'id':
                if get_object_id:
                    object_data[attr] = request_data[attr]
            elif attributes[attr]['required'] and use_require_fields:
                object_data[attr] = request_data[attr]
            else:
                object_data[attr] = request_data.get(attr)

        return object_data

    except JSONDecodeError:
        raise IncorrectBody("json")
    except KeyError as key:
        attr = key.__str__().replace("'", '')
        error = attributes[attr]
        error["attr"] = attr
        raise IncorrectBody(error)
