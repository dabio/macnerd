import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOPIC = "macnerd-topic"


def respond(code=200, body=None):
    return {
        'statusCode': code,
        'body': body
    }


def handler(event, context):
    logging.info(event)

    challenge = event.get('queryStringParameters', {}).get('hub.challenge')
    if not challenge:
        return respond(400)

    table = boto3.resource('dynamodb').Table(TOPIC)
    topic_id = event.get('pathParameters', {}).get('id')
    if not table.get_item(Key={'id': topic_id}).get('Item'):
        return respond(400)

    return respond(200, challenge)
