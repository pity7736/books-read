import unittest

from sqlalchemy.exc import InvalidRequestError

from src.models.author import AuthorModel
from src.models.base import Base, engine


class LookupAuthorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)
        bulk = (
            AuthorModel(first_name='first_name1', last_name='last_name1'),
            AuthorModel(first_name='first_name2', last_name='last_name2'),
            AuthorModel(first_name='first_name3', last_name='last_name3'),
            AuthorModel(first_name='first_name4', last_name='last_name4'),
            AuthorModel(first_name='first_name5', last_name='last_name4'),
            AuthorModel(first_name='first_name2', last_name='last_name5'),
        )
        AuthorModel.bulk_create(bulk)

    def test_get_by_id(self):
        author = AuthorModel.get(id=1)
        self.assertIsInstance(author, AuthorModel)
        self.assertEqual(author.id, 1)
        self.assertEqual(author.first_name, 'first_name1')
        self.assertEqual(author.last_name, 'last_name1')

    def test_get_by_not_exists_id(self):
        author = AuthorModel.get(id=10)
        self.assertIsNone(author)

    def test_get_by_first_name(self):
        author = AuthorModel.get(first_name='first_name1')

        self.assertEqual(author.id, 1)
        self.assertEqual(author.first_name, 'first_name1')
        self.assertEqual(author.last_name, 'last_name1')

    def test_get_by_last_name(self):
        author = AuthorModel.get(last_name='last_name1')

        self.assertEqual(author.id, 1)
        self.assertEqual(author.first_name, 'first_name1')
        self.assertEqual(author.last_name, 'last_name1')

    def test_get_by_wrong_param(self):
        try:
            AuthorModel.get(param_fail='test')
            self.fail('this should fail')
        except InvalidRequestError:
            pass

    def test_filter_by_first_name(self):
        authors = AuthorModel.filter_by(first_name='first_name2')

        self.assertEqual(authors.count(), 2)
        self.assertEqual(authors[0].first_name, 'first_name2')
        self.assertEqual(authors[1].first_name, 'first_name2')

    def test_filter_by_wrong_first_name(self):
        authors = AuthorModel.filter_by(first_name='test')

        self.assertEqual(authors.count(), 0)

    def test_filter_by_last_name(self):
        authors = AuthorModel.filter_by(last_name='last_name4')

        self.assertEqual(authors.count(), 2)
        self.assertEqual(authors[0].last_name, 'last_name4')
        self.assertEqual(authors[1].last_name, 'last_name4')

    def test_filter_by_wrong_last_name(self):
        authors = AuthorModel.filter_by(last_name='test')

        self.assertEqual(authors.count(), 0)

    def test_filter_by_wrong_param(self):
        try:
            AuthorModel.filter_by(param_fail='test')
            self.fail('this should fail')
        except InvalidRequestError:
            pass

    @classmethod
    def tearDownClass(cls):
        AuthorModel.session.close_all()
        Base.metadata.drop_all(engine)
