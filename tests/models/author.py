import unittest

from src.models.create_author import AuthorModel


class CreateAuthorModelTest(unittest.TestCase):

    def test_create_author_with_all_data(self):
        author = AuthorModel()
        author.first_name = 'name'
        author.last_name = 'name2'
        self.assertIsNone(author.save())

    def test_create_author_with_all_data_in_arguments(self):
        author = AuthorModel(first_name='first_name1', last_name='last_name1')
        self.assertIsNone(author.save())

    def test_create_author_without_first_name(self):
        author = AuthorModel()
        author.last_name = 'name'
        try:
            author.save()
            self.fail('this should fail')
        except ValueError:
            pass

    def test_create_author_without_last_name(self):
        author = AuthorModel()
        author.first_name = 'name'
        try:
            author.save()
            self.fail('this should fail')
        except ValueError:
            pass
