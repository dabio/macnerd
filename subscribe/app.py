import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Topic(object):
    def __init__(self, json_dump):
        self.id = json_dump['id']['S']
        self.topic = json_dump['topic']['S']

    def subscribe(self):
        logging.info('subscribing %s with id %s', self.topic, self.id)


def handler(event, context):
    logging.info(event)
    for item in event['Records']:
        topic = Topic(item['dynamodb']['NewImage'])
        topic.subscribe()


if __name__ == '__main__':
    with open('event.json') as f:
        handler(json.dumps(f.read()), False)
