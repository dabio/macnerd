import boto3
import json
import logging
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOPIC = 'macnerd-topic'
ITEM = 'macnerd-item'


def convert(body):
    return {
        'id': str(uuid.uuid5(uuid.NAMESPACE_DNS, body.get('id'))),
        'topic_id': body.get('topic_id'),
        'title': body.get('title'),
        'summary': body.get('summary'),
        'content': body.get('content'),
        'link': body.get('permalinkUrl'),
        'published': body.get('published'),
        'updated': body.get('updated'),
    }


def respond(code=200):
    return {
        'statusCode': code
    }


def handler(event, context):
    logging.info(event)

    resource = boto3.resource('dynamodb')
    table = resource.Table(TOPIC)

    topic = table.get_item(Key={'id': event.get('pathParameters').get('id')})
    logging.info(topic)
    if not topic.get('Item'):
        return respond(404)

    body = json.loads(event.get("body"))
    logging.info(json.dumps(body, indent=4))

    table = resource.Table(ITEM)
    with table.batch_writer() as batch:
        for item in body.get('items', []):
            item['topic_id'] = topic.get('Item').get('id')
            batch.put_item(Item=convert(item))

    return respond(200)
