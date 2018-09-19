import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

INSERT = 'INSERT'


class Topic(object):
    def __init__(self, json_dump):
        self.id = json_dump['id']['S']
        self.topic = json_dump['topic']['S']

    def subscribe(self):
        logging.info('subscribing %s with id %s', self.topic, self.id)


def handler(event, context):
    logging.info(event)
    records = [r for r in event['Records'] if r['eventName'] == INSERT]
    topics = []
    for item in records:
        topic = Topic(item['dynamodb']['NewImage'])
        topic.subscribe()
        topics.append(topic)

    return [t.id for t in topics]
