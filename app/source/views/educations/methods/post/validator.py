from datetime import datetime


def handler(request_data):
    if request_data.get('finished_at'):
        request_data['finished_at'] = datetime.strptime(request_data['finished_at'], '%Y')
    return request_data
