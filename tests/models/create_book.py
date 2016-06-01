import datetime
import unittest

from sqlalchemy.exc import IntegrityError
from src.models.author import AuthorModel

from src.models.base import Base, engine
from src.models.book import BookModel
from src.models.topic import TopicModel


class CreateBookTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)
        cls.topic = TopicModel(name='software engineering')

    def test_save_book(self):
        book = BookModel()
        book.title = 'object-oriented analysis and design with applications ' \
                     'third edition'
        book.publication_date = 2007
        book.read_date = datetime.date.today()
        book.topic = self.topic
        self.assertIsNone(book.save())

    def test_save_book_without_topic(self):
        book = BookModel(
            title='clean code',
            publication_date=2008,
            read_date=datetime.date.today()
        )
        try:
            book.save()
            self.fail('this should fail')
        except IntegrityError:
            pass

    def test_save_book_with_authors(self):
        book = BookModel(
            title='refactoring: improving the design of existing code',
            publication_date=1999,
            read_date=datetime.date.today(),
            topic_id=1
        )
        author = AuthorModel(
            first_name='martin',
            last_name='fowler'
        )
        book.authors.append(author)
        self.assertIsNone(book.save())

    def test_create_book(self):
        topic = TopicModel(name='tdd')
        topic.save()
        book = BookModel.create(
            title='test-driven development: by example',
            publication_date=2002,
            read_date=datetime.date.today(),
            topic_id=topic.id
        )
        self.assertIsNotNone(book.id)
        self.assertIsInstance(book, BookModel)

    @classmethod
    def tearDownClass(cls):
        TopicModel.session.close_all()
        Base.metadata.drop_all(engine)
