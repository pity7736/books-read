from .base import Book, Session


class BookModel(Book):
    session = Session()

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.publication_date = kwargs.get('publication_date')
        self.read_date = kwargs.get('read_date')
        self.topic_id = kwargs.get('topic_id')

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
