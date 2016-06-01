from .base import Author
from .model import Model


class AuthorModel(Author, Model):

    def __repr__(self):
        _repr = '<Author: {0}>'.format(self.get_full_name())
        if self.id:
            _repr = '<Author: {0} - {1}>'.format(self.id, self.get_full_name())

        return _repr

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
