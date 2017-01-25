import datetime
import unittest

from src import engine
from src.models import metadata, AuthorModel, BookModel, TopicModel


class SearchBookModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metadata.create_all(engine)
        # authors:
        martin_fowler = AuthorModel(first_name='martin', last_name='fowler')
        rober_martin = AuthorModel(first_name='robert', last_name='martin')
        grady_booch = AuthorModel(first_name='grady', last_name='booch')
        george_orwell = AuthorModel(first_name='george', last_name='orwell')

        # topics
        sotware_engineering = TopicModel(name='ingeniería de software')
        novel = TopicModel(name='novela')

        # books
        ooad = BookModel(
            title='object-oriented analysis and design with applications '
                  'third edition',
            publication_date=2008,
            read_date=datetime.date.today(),
            topic=sotware_engineering
        )
        refactoring = BookModel(
            title='refactoring: improving the design of existing code',
            publication_date=1999,
            read_date=datetime.date(2016, 5, 20),
            topic=sotware_engineering
        )
        clean_code = BookModel(
            title='clean code',
            publication_date=2008,
            read_date=datetime.date(2015, 11, 20),
            topic=sotware_engineering
        )
        b1984 = BookModel(
            title='1984',
            publication_date=1949,
            read_date=datetime.date.today(),
            topic=novel
        )
        ooad.authors.append(grady_booch)
        refactoring.authors.append(martin_fowler)
        clean_code.authors.append(rober_martin)
        b1984.authors.append(george_orwell)
        bulk = (
            ooad,
            refactoring,
            clean_code,
            b1984
        )
        BookModel.bulk_create(bulk)

    def test_get_by_title(self):
        book = BookModel.get(title='clean code')

        self.assertEqual(book.title, 'clean code')
        self.assertEqual(book.publication_date, 2008)
        self.assertEqual(book.topic.name, 'ingeniería de software')

    def test_filter_by_topic_name(self):
        books = BookModel.filter_by_topic(name='ingeniería de software')

        self.assertEqual(books.count(), 3)

    def test_filter_by_topic_id(self):
        books = BookModel.filter_by_topic(id=1)

        self.assertEqual(books.count(), 3)

    def test_filter_by_author_first_name(self):
        books = BookModel.filter_by_author(first_name='robert')

        self.assertEqual(books.count(), 1)
        self.assertEqual(books.first().title, 'clean code')

    def test_filter_by_author_last_name(self):
        books = BookModel.filter_by_author(last_name='martin')

        self.assertEqual(books.count(), 1)
        self.assertEqual(books.first().title, 'clean code')

    @classmethod
    def tearDownClass(cls):
        BookModel.session.close_all()
        metadata.drop_all(engine)
