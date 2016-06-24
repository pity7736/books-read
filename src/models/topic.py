from .base import Topic
from .model import Model


class TopicModel(Topic, Model):

    def __repr__(self):
        _repr = '<Topic: {0} - {1}>'.format(self.id, self.name)
        return _repr

    @classmethod
    def filter_by_name(cls, name):
        topics = cls.session.query(cls).filter(
            cls.name.like('%{0}%'.format(name))
        )
        return topics
