import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

INSERT = 'INSERT'


class Topic(object):
    def __init__(self, json_dump):
        self.id = json_dump.get('id').get('S')
        self.topic = json_dump.get('topic').get('S')

    def subscribe(self):
        logging.info('subscribing %s with id %s', self.topic, self.id)


def handler(event, context):
    logging.info(event)
    records = [r for r in event.get('Records') if r.get('eventName') == INSERT]
    topics = []
    for item in records:
        topic = Topic(item.get('dynamodb').get('NewImage'))
        topic.subscribe()
        topics.append(topic)

    return [t.id for t in topics]
