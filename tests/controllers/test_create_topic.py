import unittest
from unittest.mock import patch

from src.controllers import CreateTopicController
from src.models.topic import TopicModel


class CreateTopicControllerTests(unittest.TestCase):

    def test_create_topic(self):
        with patch.object(TopicModel, 'save') as mock_topic_model:
            create_topic_controller = CreateTopicController(name='test')
            create_topic_controller.save()

        self.assertIs(mock_topic_model.called, True)
        self.assertEqual(mock_topic_model.call_count, 1)
