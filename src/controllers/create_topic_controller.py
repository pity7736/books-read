from ..models import TopicModel


class CreateTopicController:

    def __init__(self, name):
        self.model = TopicModel(name=name)

    def save(self):
        self.model.save()
