import unittest

from doublex import Mock, assert_that, verify

from src.controllers import CreateAuthorController


class CreateAuthorControllerTests(unittest.TestCase):

    def test_create_author(self):
        with Mock(CreateAuthorController) as mock:
            mock.save().returns(None).times(1)

        mock.save()
        assert_that(mock, verify())
