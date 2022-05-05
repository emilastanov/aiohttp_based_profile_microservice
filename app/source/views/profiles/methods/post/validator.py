from datetime import datetime

from app.middlewares.errors import IncorrectBody


def handler(request_data):
    try:
        request_data['registered_at'] = datetime.now()
        request_data['date_of_birthday'] = datetime.strptime(request_data['date_of_birthday'], "%Y-%m-%d")
    except ValueError as error:
        raise IncorrectBody(error)

    return request_data
