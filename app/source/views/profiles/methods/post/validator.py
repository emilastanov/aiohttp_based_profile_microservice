from datetime import datetime

from app.middlewares.errors import IncorrectBody


def handler(request_data):
    try:
        if request_data.get('id') is None:
            request_data['registered_at'] = datetime.now()
        if request_data.get('date_of_birthday'):
            request_data['date_of_birthday'] = datetime.strptime(request_data['date_of_birthday'], "%Y-%m-%d")
    except ValueError as error:
        raise IncorrectBody(error)

    return request_data
