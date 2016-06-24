import unittest

from doublex import Stub, assert_that, is_, ANY_ARG
from sqlalchemy.orm.query import Query

from src.controllers import SearchTopicsController
from src.models.topic import TopicModel


class SearchTopicsTest(unittest.TestCase):

    # bulk = (
    #     TopicModel(name='ingeniería de software'),
    #     TopicModel(name='ingeniería industrial'),
    #     TopicModel(name='ingeniería ambiental'),
    #     TopicModel(name='psicología'),
    #     TopicModel(name='inteligencia artificial')
    # )
    # TopicModel.bulk_create(bulk)

    def test_get_by_name(self):
        with Stub(TopicModel) as stub_model:
            stub_model.name = 'ingeniería de software'

        with Stub(SearchTopicsController) as stub_contoller:
            stub_contoller.get_by_name(ANY_ARG).returns(stub_model)

        topic = stub_contoller.get_by_name('ingeniería de sofware')

        assert_that(topic.name, is_('ingeniería de software'))

    def test_search_by_name(self):
        with Stub(Query) as stub_query:
            stub_query.count().returns(3)

        with Stub(SearchTopicsController) as stub_controller:
            stub_controller.filter_by_name('ingeniería').returns(stub_query)

        topics = stub_controller.filter_by_name('ingeniería')

        assert_that(topics.count(), is_(3))
