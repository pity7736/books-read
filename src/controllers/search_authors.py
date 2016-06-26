from ..models import AuthorModel


class SearchAuthorsController:
    model = AuthorModel

    def filter_by(self, **kwargs):
        authors = self.model.filter_by(**kwargs)
        return authors

    def filter_by_name(self, name):
        authors = self.model.filter_by_name(name)
        return authors
