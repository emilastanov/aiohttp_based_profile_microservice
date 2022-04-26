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

UNKNOWN_TOKEN = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Unknown user token.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

UNKNOWN_FILE = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Unknown file.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

UNKNOWN_HTML_TEMPLATE = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Unknown html template.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

USER_DOES_NOT_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'User does not exits.'
        }
    },
    'status': web.HTTPNotFound.status_code
}

INCORRECT_PASSWORD = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'User does not exits.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

UNKNOWN_USER_ROLE = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Unknown user role.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

PERMISSION_DENIED = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Permission denied.'
        }
    },
    'status': web.HTTPForbidden.status_code
}

USER_ALREADY_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'User already exist.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

ROLE_ALREADY_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Role already exist.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

FILE_ALREADY_EXIST = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'File already exist.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

EMAIL_ALREADY_CHECKED = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Current user email is already checked.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

PHONE_ALREADY_CHECKED = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Current user phone is already checked.'
        }
    },
    'status': web.HTTPBadRequest.status_code
}

VERIFICATION_CODE_EXPIRED = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Verification code expired.'
        }
    },
    'status': web.HTTPForbidden.status_code
}

INCORRECT_VERIFICATION_CODE = {
    'data': {
        'status': 'error',
        'data': {
            'error': 'Incorrect verification code.'
        }
    },
    'status': web.HTTPForbidden.status_code
}


def token_expired(data):
    return {
        "data": {
            "status": "deleted",
            "data": data
        },
        "status": web.HTTPUnauthorized.status_code
    }
