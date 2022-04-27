from aiohttp import web

INCORRECT_REQUEST_BODY = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Incorrect request body.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

INCORRECT_PLATFORM = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Incorrect platform.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

UNKNOWN_OBJECT = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Unknown object.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

OBJECT_DOES_NOT_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Object does not exits.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

OBJECT_ALREADY_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Object already exist.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}
