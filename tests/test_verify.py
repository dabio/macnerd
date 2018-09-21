import pytest
from verify import app


CHALLENGE = 'olnkk73345qmdmhlrf6r'


def test_success(success_event):
    ret = app.handler(success_event, "")
    assert ret.get('statusCode') == 200
    assert ret.get('body') == CHALLENGE


@pytest.fixture()
def success_event():
    """ Generates API GW Event"""

    return {
        'pathParameters': {
            'id': '1956576f-c82a-49d3-b23e-0eb9c5dde718'
        },
        "queryStringParameters": {
            "hub.challenge": CHALLENGE,
            "hub.lease_seconds": "315360000",
            "hub.mode": "subscribe",
            "hub.topic": "https://daringfireball.net/feeds/main"
        }
    }


def test_no_challenge(no_challenge_event):
    ret = app.handler(no_challenge_event, "")
    assert ret.get('statusCode') == 400
    assert ret.get('body') is None


@pytest.fixture()
def no_challenge_event():
    """ Generates API GW Event"""

    return {
        'pathParameters': {
            'id': '1956576f-c82a-49d3-b23e-0eb9c5dde718'
        }
    }


def test_wrong_topic_id(wrong_topic_id_event):
    ret = app.handler(wrong_topic_id_event, "")
    assert ret.get('statusCode') == 400
    assert ret.get('body') is None


@pytest.fixture()
def wrong_topic_id_event():
    """ Generates API GW Event"""

    return {
        'pathParameters': {
            'id': '2be193d3-96f7-4bea-a48d-e8edc21b2731'
        }
    }
