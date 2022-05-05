from app.source import models


def get_object_attributes(model):
    model = getattr(models, ''.join([word.capitalize() for word in model.split('_')]))
    attributes = {}
    for attribute in [
                         key
                         for key in model.__dict__.keys()
                         if '__' not in key
                     ][:-1]:
        attributes[attribute] = {
            'required': not model
                .__dict__[attribute]
                .__dict__['column'].nullable,
            'type': str(model
                .__dict__[attribute]
                .__dict__['column']
                .__dict__['type']).upper()
        }
    return attributes
