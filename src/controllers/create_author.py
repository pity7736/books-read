from ..models import AuthorModel


class CreateAuthorController:
    def __init__(self, first_name, last_name):
        self.model = AuthorModel(first_name=first_name, last_name=last_name)

    def save(self):
        self.model.save()
