import unittest

from doublex import Stub, assert_that, is_, ANY_ARG
from sqlalchemy.orm.query import Query

from src.controllers import SearchAuthorsController
from src.models import AuthorModel


class SearchAuthorsTest(unittest.TestCase):
    # bulk = (
    #     AuthorModel(first_name='martin', last_name='fowler'),
    #     AuthorModel(first_name='robert', last_name='martin'),
    #     AuthorModel(first_name='kent', last_name='beck'),
    #     AuthorModel(first_name='gerard', last_name='meszaros'),
    #     AuthorModel(first_name='erich', last_name='gamma')
    # )
    # AuthorModel.bulk_create(bulk)

    def test_filter_by_first_name(self):
        with Stub(Query) as stub_model:
            stub_model.count().returns(1)

        with Stub(SearchAuthorsController) as stub_contoller:
            stub_contoller.filter_by(ANY_ARG).returns(stub_model)

        authors = stub_contoller.filter_by(first_name='gerard')

        assert_that(authors.count(), is_(1))

    def test_filter_by_last_name(self):
        with Stub(Query) as stub_model:
            stub_model.count().returns(1)

        with Stub(SearchAuthorsController) as stub_contoller:
            stub_contoller.filter_by(ANY_ARG).returns(stub_model)

        authors = stub_contoller.filter_by(last_name='gamma')

        assert_that(authors.count(), is_(1))

    def test_filter_by_first_name_or_last_name(self):
        with Stub(Query) as stub_model:
            stub_model.count().returns(2)

        with Stub(SearchAuthorsController) as stub_contoller:
            stub_contoller.filter_by_name(ANY_ARG).returns(stub_model)

        authors = stub_contoller.filter_by_name('martin')

        assert_that(authors.count(), is_(2))

