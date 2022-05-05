from asyncpg import DataError, ForeignKeyViolationError
from sqlalchemy.exc import StatementError

from app.middlewares.errors import IncorrectBody
from app.middlewares.objects.attributes import get_object_attributes
from app.middlewares.objects.request import get_request_json_body


async def handler(request, model, validator=lambda res: res, simultaneously_create=None):
    attributes = get_object_attributes(model)

    request_data = validator(await get_request_json_body(request, attributes))

    try:
        _object = await getattr(request.app['db'], model).create(**request_data)
        if simultaneously_create:
            return simultaneously_create(request_data, _object)
        return _object

    except StatementError as error:
        raise IncorrectBody(error)

    except DataError as error:
        raise IncorrectBody(error)

    except ForeignKeyViolationError as error:
        raise IncorrectBody(error)
