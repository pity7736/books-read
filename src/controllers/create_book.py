from ..models import BookModel


class CreateBookController:
    def __init__(self, title, publication_date, read_date, topic_id=None,
                 topic=None):
        assert topic or topic_id, 'Topic or Topic_id is obligatory'

        self.model = BookModel(
            title=title,
            publication_date=publication_date,
            read_date=read_date,
            topic=topic,
            topic_id=topic_id
        )

    def save(self):
        self.model.save()

