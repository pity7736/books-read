import unittest

from src import engine
from src.models import metadata, TopicModel


class SearchTopicModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metadata.create_all(engine)
        bulk = (
            TopicModel(name='ingeniería de software'),
            TopicModel(name='ingeniería industrial'),
            TopicModel(name='ingeniería ambiental'),
            TopicModel(name='psicología'),
            TopicModel(name='inteligencia artificial')
        )
        TopicModel.bulk_create(bulk)

    def test_filter_by_containts_name(self):
        topics = TopicModel.filter_by_name('ingeniería')

        self.assertEqual(topics.count(), 3)

    @classmethod
    def tearDownClass(cls):
        TopicModel.session.close_all()
        metadata.drop_all(engine)
