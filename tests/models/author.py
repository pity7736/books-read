import unittest

from src.models.author import AuthorModel


class AuthorModelTest(unittest.TestCase):

    def setUp(self):
        self.author = AuthorModel()

    def test_add_author_with_all_data(self):
        self.author.first_name = 'julián'
        self.author.last_name = 'cortés'

        self.assertIsNone(self.author.save())
        self.assertEqual(self.author.id, 1)

    def test_add_two_author(self):
        author1 = AuthorModel()
        author1.first_name = 'ernesto'
        author1.last_name = 'vergel'
        author1.save()
        author2 = AuthorModel()
        author2.first_name = 'julián'
        author2.last_name = 'vergel'
        author2.save()
        self.assertEqual(author1.id, 1)
        self.assertEqual(author2.id, 2)

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
