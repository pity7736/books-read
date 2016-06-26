from ..models import BookModel


class SearchBooksController:
    model = BookModel

    def get_by_title(self, title):
        book = self.model.get(title=title)
        return book
