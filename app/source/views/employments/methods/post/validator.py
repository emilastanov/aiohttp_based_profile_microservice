from datetime import datetime

from app.middlewares.errors import IncorrectBody


def handler(request_data):
    try:
        if request_data.get('finished_at'):
            request_data['finished_at'] = datetime.strptime(request_data['finished_at'], "%Y-%m-%d")
        if request_data.get('started_at'):
            request_data['started_at'] = datetime.strptime(request_data['started_at'], "%Y-%m-%d")
    except ValueError as error:
        raise IncorrectBody(error)

    return request_data
