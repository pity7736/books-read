from .. import Session

class Model:
    id = None
    session = Session()

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj

    def save(self):
        self.session.add(self)
        self._commit()

    @classmethod
    def bulk_create(cls, bulk):
        cls.session.add_all(bulk)
        cls._commit()

    @classmethod
    def _commit(cls):
        try:
            cls.session.commit()
        except:
            cls.session.rollback()
            raise

    @classmethod
    def get(cls, **kwargs):
        obj = cls.filter_by(**kwargs).one()
        return obj

    @classmethod
    def filter_by(cls, **kwargs):
        objects = cls.session.query(cls).filter_by(**kwargs)
        return objects

    @classmethod
    def get_all(cls):
        objects = cls.session.query(cls)
        return objects
