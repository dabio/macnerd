import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(event)
    if not event['multiValueQueryStringParameters']:
        return {
            'statusCode': '400'
        }
    if not event['multiValueQueryStringParameters']['hub.challenge']:
        return {
            'statusCode': '400'
        }

    return {
        'statusCode': '200',
        'body': event['multiValueQueryStringParameters']['hub.challenge'][0]
    }


if __name__ == '__main__':
    with open('event.json') as f:
        handler(json.loads(f.read()), False)
