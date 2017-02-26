import unittest
from unittest.mock import patch

from src.controllers import CreateBookController
from src.models.book import BookModel


class CreateAuthorControllerTests(unittest.TestCase):
    def test_create_author(self):
        with patch.object(BookModel, 'save') as mock_book_model:
            create_book_controller = CreateBookController(
                title='test',
                publication_date='2017',
                read_date='2017-02-25',
                topic_id=1
            )
            create_book_controller.save()

        self.assertIs(mock_book_model.called, True)
        self.assertEqual(mock_book_model.call_count, 1)
