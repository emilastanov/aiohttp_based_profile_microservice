from datetime import datetime

from app.middlewares.errors import IncorrectBody


def handler(request_data):
    if request_data.get('finished_at'):
        try:
            request_data['finished_at'] = datetime.strptime(request_data['finished_at'], '%Y')
        except ValueError as error:
            raise IncorrectBody(error)
    return request_data
