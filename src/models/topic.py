from .base import Topic
from .model import Model


class TopicModel(Topic, Model):

    def __repr__(self):
        _repr = '<Topic: {0}>'.format(self.name)
        if self.id:
            _repr = '<Topic: {0} - {1}>'.format(self.id, self.name)

        return _repr
