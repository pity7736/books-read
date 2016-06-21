import unittest

from doublex import Mock, assert_that, verify

from src.controllers import CreateTopicController


class CreateTopicControllerTests(unittest.TestCase):

    def test_create_topic(self):
        with Mock(CreateTopicController('test')) as mock:
            mock.save().returns(None).times(1)

        mock.save()
        assert_that(mock, verify())
