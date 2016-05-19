
class AuthorModel:
    id = None
    first_name = ''
    last_name = ''
    _intances = {}

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def save(self):
        if not self.first_name or not self.last_name:
            raise ValueError('first_name is obligatory')

        self.id = len(self._intances) + 1
        self._intances[str(self.id)] = self

    @classmethod
    def get(cls, id):
        author = cls._intances[str(id)]
        return author

    @classmethod
    def filter_by_first_name(cls, name):
        authors = list()
        for author in cls._intances.values():
            if author.first_name == name:
                authors.append(author)

        return authors
