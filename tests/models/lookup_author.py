import unittest

from src.models.author import AuthorModel
from src.models.base import engine, Base


class LookupAuthorTests(unittest.TestCase):

    def setUp(self):
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
    #
    # def test_filter_by_first_name(self):
    #     authors = AuthorModel.filter_by_first_name('first_name2')
    #
    #     self.assertEqual(len(authors), 2)
    #     self.assertEqual(authors[0].first_name, 'first_name2')
    #     self.assertEqual(authors[1].first_name, 'first_name2')
    #
    # def test_filter_by_wrong_first_name(self):
    #     authors = AuthorModel.filter_by_first_name('test')
    #
    #     self.assertEqual(len(authors), 0)
    #
    # def test_filter_by_last_name(self):
    #     authors = AuthorModel.filter_by_last_name('last_name4')
    #
    #     self.assertEqual(len(authors), 2)
    #     self.assertEqual(authors[0].last_name, 'last_name4')
    #     self.assertEqual(authors[1].last_name, 'last_name4')
    #
    # def test_filter_by_wrong_last_name(self):
    #     authors = AuthorModel.filter_by_last_name('test')
    #
    #     self.assertEqual(len(authors), 0)

    def tearDown(self):
        AuthorModel.session.close_all()
        Base.metadata.drop_all(engine)
