import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(event)
    return {
        'statusCode': '200'
    }


if __name__ == '__main__':
    with open('event.json') as f:
        handler(json.loads(f.read()), False)
