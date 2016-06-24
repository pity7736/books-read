from ..models.topic import TopicModel


class SearchTopicsController:

    def get_by_name(self, name):
        topic = TopicModel.get(name=name)
        return topic

    def filter_by_name(self, name):
        topics = TopicModel.session.query(TopicModel).filter(
            TopicModel.name.like('%{0}%'.format(name))
        )
        return topics
