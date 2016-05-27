from .base import Author, Session


class AuthorModel(Author):
    session = Session()

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

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
        author = cls(**kwargs)
        author.save()
        return author

    @classmethod
    def bulk_create(cls, bulk):
        cls.session.add_all(bulk)
        cls._commit()

    @classmethod
    def get(cls, **kwargs):
        author = cls.session.query(cls).filter_by(**kwargs).first()
        return author

    @classmethod
    def filter(cls, **kwargs):
        authors = cls.session.query(cls).filter_by(**kwargs)
        return authors
