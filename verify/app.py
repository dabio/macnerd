import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(event)
    if not event['queryStringParameters']:
        return {
            'statusCode': 400
        }
    if not event['queryStringParameters']['hub.challenge']:
        return {
            'statusCode': 400
        }

    return {
        'statusCode': 200,
        'body': event['queryStringParameters']['hub.challenge']
    }
