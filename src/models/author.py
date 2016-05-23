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
        try:
            cls.session.commit()
        except:
            cls.session.rollback()
            raise

    @classmethod
    def get(cls, author_id):
        author = cls._intances[str(author_id)]
        return author

    @classmethod
    def filter_by_first_name(cls, name):
        authors = list()
        for author in cls._intances.values():
            if author.first_name == name:
                authors.append(author)

        return authors

    @classmethod
    def filter_by_last_name(cls, name):
        authors = list()
        for author in cls._intances.values():
            if author.last_name == name:
                authors.append(author)

        return authors
