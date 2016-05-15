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
        author2.last_name = 'cortés'
        author2.save()
        self.assertEqual(author1.id, 2)
        self.assertEqual(author2.id, 3)

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

    def test_get_author_by_id(self):
        self.author.first_name = 'nombre'
        self.author.last_name = 'apellido'
        self.author.save()

        author = AuthorModel.get(id=4)

        self.assertEqual(author.first_name, 'nombre')
        self.assertEqual(author.last_name, 'apellido')
        self.assertEqual(author.id, 4)

    def test_get_author_by_wrong_id(self):
        try:
            AuthorModel.get(id=10)
            self.fail('this should fail')
        except KeyError:
            pass

    def test_get_authors_by_first_name(self):
        author1 = AuthorModel()
        author1.first_name = 'julián'
        author1.last_name = 'vergel'
        author1.save()
        author2 = AuthorModel()
        author2.first_name = 'julián'
        author2.last_name = 'cortés'
        author2.save()

        authors = AuthorModel.filter_by_first_name('julián')

        self.assertEqual(authors[0].first_name, 'julián')
        self.assertEqual(authors[1].first_name, 'julián')

if __name__ == '__main__':
    print('hola')
    unittest.main()
