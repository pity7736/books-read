import unittest

from sqlalchemy.exc import IntegrityError

from src.models.base import Base, engine
from src.models.topic import TopicModel


class CreateTopicModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)

    def test_save_topic(self):
        topic = TopicModel()
        topic.name = 'topic 1'
        self.assertIsNone(topic.save())

    def test_save_topic_with_name_in_argument(self):
        topic = TopicModel(name='new topic')
        self.assertIsNone(topic.save())

    def test_save_topic_without_name(self):
        topic = TopicModel()
        try:
            topic.save()
            self.fail('this should fail')
        except IntegrityError:
            pass

    def test_create_topic(self):
        topic = TopicModel.create(name='create topic')
        self.assertIsNotNone(topic.id)
        self.assertIsInstance(topic, TopicModel)

    def test_create_topic_without_name(self):
        try:
            TopicModel.create()
            self.fail('this should fail')
        except IntegrityError:
            pass

    @classmethod
    def tearDownClass(cls):
        TopicModel.session.close_all()
        Base.metadata.drop_all(engine)

