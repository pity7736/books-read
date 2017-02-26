import unittest

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from src import engine
from src.models import metadata, AuthorModel


class SearchAuthorModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metadata.create_all(engine)
        bulk = (
            AuthorModel(first_name='martin', last_name='fowler'),
            AuthorModel(first_name='robert', last_name='martin'),
            AuthorModel(first_name='kent', last_name='beck'),
            AuthorModel(first_name='gerard', last_name='meszaros'),
            AuthorModel(first_name='erich', last_name='gamma')
        )
        AuthorModel.bulk_create(bulk)

    def test_get_by_id(self):
        author = AuthorModel.get(id=1)
        self.assertIsInstance(author, AuthorModel)
        self.assertEqual(author.id, 1)
        self.assertEqual(author.first_name, 'martin')
        self.assertEqual(author.last_name, 'fowler')

    def test_get_by_nonexistent_id(self):
        try:
            AuthorModel.get(id=10)
            self.fail('this should fail')
        except NoResultFound:
            pass

    def test_get_by_first_name(self):
        author = AuthorModel.get(first_name='robert')

        self.assertEqual(author.id, 2)
        self.assertEqual(author.first_name, 'robert')
        self.assertEqual(author.last_name, 'martin')

    def test_get_by_last_name(self):
        author = AuthorModel.get(last_name='beck')

        self.assertEqual(author.id, 3)
        self.assertEqual(author.first_name, 'kent')
        self.assertEqual(author.last_name, 'beck')

    def test_get_by_nonexistent_param(self):
        try:
            AuthorModel.get(nonexistent_param='test')
            self.fail('this should fail')
        except InvalidRequestError:
            pass

    def test_filter_by_first_name(self):
        authors = AuthorModel.filter_by(first_name='gerard')

        self.assertEqual(authors.count(), 1)
        self.assertEqual(authors[0].first_name, 'gerard')

    def test_filter_by_nonexistent_first_name(self):
        authors = AuthorModel.filter_by(first_name='test')

        self.assertEqual(authors.count(), 0)

    def test_filter_by_last_name(self):
        authors = AuthorModel.filter_by(last_name='gamma')

        self.assertEqual(authors.count(), 1)
        self.assertEqual(authors[0].last_name, 'gamma')

    def test_filter_by_nonexistent_last_name(self):
        authors = AuthorModel.filter_by(last_name='test')

        self.assertEqual(authors.count(), 0)

    def test_filter_by_nonexistent_param(self):
        try:
            AuthorModel.filter_by(nonexistent_param='test')
            self.fail('this should fail')
        except InvalidRequestError:
            pass

    def test_filter_by_first_name_or_last_name(self):
        authors = AuthorModel.filter_by_name('martin')

        self.assertEqual(authors.count(), 2)
        self.assertIn('martin', (authors[0].first_name, authors[0].last_name))
        self.assertIn('martin', (authors[1].first_name, authors[1].last_name))

    @classmethod
    def tearDownClass(cls):
        AuthorModel.session.close_all()
        metadata.drop_all(engine)
