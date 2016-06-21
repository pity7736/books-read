from .base import Book
from .model import Model


class BookModel(Book, Model):

    def __repr__(self):
        _repr = '<Book: {0} - {1}>'.format(self.id, self.title)
        return _repr
