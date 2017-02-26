import unittest
from unittest.mock import patch

from src.controllers import CreateAuthorController
from src.models.author import AuthorModel


class CreateAuthorControllerTests(unittest.TestCase):

    # @patch('src.models.author.AuthorModel.save')
    def test_create_author(self):
        with patch.object(AuthorModel, 'save') as mock_author_model:
            create_author_controller = CreateAuthorController(
                first_name='julián',
                last_name='cortés'
            )
            create_author_controller.save()

        self.assertIs(mock_author_model.called, True)
        self.assertEqual(mock_author_model.call_count, 1)
