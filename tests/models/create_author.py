import unittest

from src.models.author import AuthorModel


class CreateAuthorModelTest(unittest.TestCase):

    def test_save_author_with_all_data(self):
        author = AuthorModel()
        author.first_name = 'name'
        author.last_name = 'name2'
        self.assertIsNone(author.save())

    def test_save_author_with_all_data_in_arguments(self):
        author = AuthorModel(first_name='first_name1', last_name='last_name1')
        self.assertIsNone(author.save())

    def test_save_author_without_first_name(self):
        author = AuthorModel()
        author.last_name = 'name'
        try:
            author.save()
            self.fail('this should fail')
        except ValueError:
            pass

    def test_save_author_without_last_name(self):
        author = AuthorModel()
        author.first_name = 'name'
        try:
            author.save()
            self.fail('this should fail')
        except ValueError:
            pass

    def test_create_author_with_all_data(self):
        author = AuthorModel.create(
            first_name='first_name2',
            last_name='last_name2'
        )
        self.assertIsInstance(author, AuthorModel)
        self.assertIsNotNone(author.id)

    def test_create_author_without_first_name(self):
        try:
            AuthorModel.create(last_name='last_name')
            self.fail('this should fail')
        except ValueError:
            pass

    def test_create_author_without_last_name(self):
        try:
            AuthorModel.create(first_name='first_name')
            self.fail('this should fail')
        except ValueError:
            pass

    def test_bulk_create(self):
        bulk = (
            {'first_name': 'first_name1', 'last_name': 'last_name1'},
            {'first_name': 'first_name2', 'last_name': 'last_name2'},
            {'first_name': 'first_name3', 'last_name': 'last_name3'},
            {'first_name': 'first_name4', 'last_name': 'last_name4'},
        )
        authors = AuthorModel.bulk_create(bulk)

        self.assertEqual(len(authors), 4)
        for author in authors:
            self.assertIsInstance(author, AuthorModel)
