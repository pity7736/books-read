from .model import Model
from ..models import TopicModel


class BookModel(Model):

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.publication_date = kwargs.get('publication_date')
        self.read_date = kwargs.get('read_date')
        topic_id = kwargs.get('topic_id')
        topic = kwargs.get('topic')
        if topic:
            self.topic = topic
        elif topic_id:
            self.topic_id = topic_id

    def __repr__(self):
        _repr = '<Book: {0} - {1}>'.format(self.id, self.title)
        return _repr

    @classmethod
    def filter_by_topic(cls, **kwargs):
        books = cls.session.query(cls).join(TopicModel).\
            filter_by(**kwargs)
        return books

    @classmethod
    def filter_by_author(cls, **kwargs):
        books = cls.session.query(cls).\
            filter(cls.authors.any(**kwargs))
        return books
