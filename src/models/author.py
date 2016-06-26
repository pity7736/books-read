from .model import Model


class AuthorModel(Model):

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def __repr__(self):
        _repr = '<Author: {0} - {1}>'.format(self.id, self.get_full_name())
        return _repr

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
