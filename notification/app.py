import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(event['path'])
    return {}


if __name__ == '__main__':
    with open('event.json') as f:
        handler(json.loads(f.read()), False)
