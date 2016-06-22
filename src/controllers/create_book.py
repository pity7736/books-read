from ..models import BookModel


class CreateBookController:
    def __init__(self, title, publication_date, read_date, topic_id):
        self.model = BookModel(
            title=title,
            publication_date=publication_date,
            read_date=read_date,
            topic_id=topic_id
        )

    def save(self):
        self.model.save()

