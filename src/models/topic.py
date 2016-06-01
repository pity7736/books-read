from .base import Topic, Session


class TopicModel(Topic):
    session = Session()

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

    @classmethod
    def _commit(cls):
        try:
            cls.session.commit()
        except:
            cls.session.rollback()
            raise

    def save(self):
        self.session.add(self)
        self._commit()

    @classmethod
    def create(cls, **kwargs):
        topic = cls(**kwargs)
        topic.save()
        return topic
