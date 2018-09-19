import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(event)
    if not event.get('queryStringParameters'):
        return {
            'statusCode': 400
        }
    if not event.get('queryStringParameters').get('hub.challenge'):
        return {
            'statusCode': 400
        }

    return {
        'statusCode': 200,
        'body': event.get('queryStringParameters').get('hub.challenge')
    }
