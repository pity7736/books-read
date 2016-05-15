
class AuthorModel:
    first_name = ''
    last_name = ''

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def save(self):
        if not self.first_name or not self.last_name:
            raise ValueError('first_name is obligatory')

        return None
