import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logging.info(json.dumps(json.loads(event.get("body")), indent=4))
    return {
        'statusCode': 200
    }
