import unittest

from doublex import Stub, assert_that, is_, ANY_ARG

from src.controllers import SearchBooksController
from src.models import BookModel


class SearchAuthorControllerTest(unittest.TestCase):
    # # authors:
    # martin_fowler = AuthorModel(first_name='martin', last_name='fowler'),
    # rober_martin = AuthorModel(first_name='robert', last_name='martin'),
    # grady_booch = AuthorModel(first_name='grady', last_name='booch'),
    # george_orwell = AuthorModel(first_name='george', last_name='orwell'),
    #
    # # topics
    # sotware_engineering = TopicModel(name='ingeniería de software'),
    # novel = TopicModel(name='novela'),
    #
    # # books
    # ooad = BookModel(
    #     title='object-oriented analysis and design with applications ' \
    #           'third edition',
    #     publication_date=2008,
    #     read_date=datetime.date.today(),
    #     topic=software_engineering
    # )
    # refactoring = BookModel(
    #     title='refactoring: improving the design of existing code',
    #     publication_date=1999,
    #     read_date=datetime.date(2016, 5, 20),
    #     topic=sotware_engineering
    # )
    # clean_code = BookModel(
    #     title='clean code',
    #     publication_date=2008,
    #     read_date=datetime.date(2015, 11, 20),
    #     topic=sotware_engineering
    # )
    # b1984 = BookModel(
    #     title='1984',
    #     publication_date=1949,
    #     read_date=datetime.date.today(),
    #     topic=novel
    # )
    # bulk = (
    #     ooad,
    #     refactoring,
    #     clean_code,
    #     b1984
    # )
    # BookModel.bulk_create(bulk)
    # ooad.authors.append(grady_booch)
    # refactoring.authors.append(martin_fowler)
    # clean_code.authors.append(rober_martin)
    # b1984.authors.append(george_orwell)

    def test_get_by_title(self):
        with Stub(BookModel) as stub_model:
            stub_model.title = 'clean code'

        with Stub(SearchBooksController) as stub_contoller:
            stub_contoller.get_by_title(ANY_ARG).returns(stub_model)

        book = stub_contoller.get_by_title(title='clean code')

        assert_that(book.title, is_('clean code'))
