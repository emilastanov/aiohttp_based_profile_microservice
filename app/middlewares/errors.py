

class UnknownObject(Exception):
    """Requested unknown object."""
    pass


class NoId(Exception):
    """Query params is not contain id."""
    pass


class IncorrectBody(Exception):
    """Body of request is incorrect."""
    pass
