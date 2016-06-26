from .model import Model


class BookModel(Model):

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.publication_date = kwargs.get('publication_date')
        self.read_date = kwargs.get('read_date')
        self.topic_id = kwargs.get('topic_id')

    def __repr__(self):
        _repr = '<Book: {0} - {1}>'.format(self.id, self.title)
        return _repr
