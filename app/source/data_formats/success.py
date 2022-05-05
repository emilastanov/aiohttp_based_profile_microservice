from aiohttp import web

DELETED = {
    "data": {
        "status": "deleted"
    },
    "status": web.HTTPAccepted.status_code
}


SUCCESS = {
    "data": {
        "status": "ok"
    },
    "status": web.HTTPOk.status_code
}


def query_data(data, **additional_args):
    response = {
        "data": {
            "status": "ok",
            "data": data
        },
        "status": web.HTTPOk.status_code
    }
    if additional_args:
        for key in additional_args:
            response["data"][key] = additional_args[key]
    return response


def data_updated(data):
    return {
        "data": {
            "status": "ok",
            "data": data
        },
        "status": web.HTTPAccepted.status_code
    }


def data_created(data):
    return {
        "data": {
            "status": "ok",
            "data": data
        },
        "status": web.HTTPCreated.status_code
    }

