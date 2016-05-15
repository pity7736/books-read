import unittest

from src.models.author import AuthorModel


class AuthorModelTest(unittest.TestCase):

    def setUp(self):
        self.author = AuthorModel()

    def test_add_author_with_all_data(self):
        self.author.first_name = 'julián'
        self.author.last_name = 'cortés'

        self.assertIsNone(self.author.save())

    def test_add_author_without_first_name(self):
        self.author.last_name = 'cortés'
        try:
            self.author.save()
            self.fail('this should fail')
        except ValueError:
            pass

    def test_add_author_without_last_name(self):
        self.author.first_name = 'julián'
        try:
            self.author.save()
            self.fail('this should fail')
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()
