from app.source import models


def get_model_by_name(name):
    return getattr(models, ''.join([word.capitalize() for word in name.split('_')]))
