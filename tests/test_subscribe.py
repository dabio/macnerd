import pytest
from subscribe import app


def test_lambda_handler(dynamodb_event):
    ret = app.handler(dynamodb_event, "")
    assert ret[0] == "5d15789d-e3db-419f-855b-89ce3e75082f"
    assert ret[1] == "ac793191-c143-4762-90b7-cc75e382d5c0"


@pytest.fixture()
def dynamodb_event():
    """ Generates DynamoDB Event"""

    return {
        "Records": [
            {
                "eventID": "62fc2326fe8dc06c8c4daccb2a53d635",
                "eventName": "INSERT",
                "eventVersion": "1.1",
                "eventSource": "aws:dynamodb",
                "awsRegion": "eu-west-1",
                "dynamodb": {
                    "ApproximateCreationDateTime": 1537350420,
                    "Keys": {
                        "id": {"S": "5d15789d-e3db-419f-855b-89ce3e75082f"}
                    },
                    "NewImage": {
                        "topic": {
                            "S": "https://daringfireball.net/feeds/main"
                        },
                        "id": {"S": "5d15789d-e3db-419f-855b-89ce3e75082f"},
                    },
                    "SequenceNumber": "100000000025935825477",
                    "SizeBytes": 118,
                    "StreamViewType": "NEW_IMAGE",
                },
                "eventSourceARN": "",
            },
            {
                "eventID": "705864f8bd574187a15285e1b35482f0",
                "eventName": "UPDATE",
                "eventVersion": "1.1",
                "eventSource": "aws:dynamodb",
                "awsRegion": "eu-west-1",
                "dynamodb": {
                    "ApproximateCreationDateTime": 1537350421,
                    "Keys": {
                        "id": {"S": "7d3c699f-783e-4461-8232-34007471483f"}
                    },
                    "NewImage": {
                        "topic": {
                            "S": "https://daringfireball.net/feeds/main"
                        },
                        "id": {"S": "7d3c699f-783e-4461-8232-34007471483f"},
                    },
                    "SequenceNumber": "100000000025935825478",
                    "SizeBytes": 118,
                    "StreamViewType": "NEW_IMAGE",
                },
                "eventSourceARN": "",
            },
            {
                "eventID": "ad58fa50e5e04dbaa2e83d37f1988300",
                "eventName": "INSERT",
                "eventVersion": "1.1",
                "eventSource": "aws:dynamodb",
                "awsRegion": "eu-west-1",
                "dynamodb": {
                    "ApproximateCreationDateTime": 1537350422,
                    "Keys": {
                        "id": {"S": "ac793191-c143-4762-90b7-cc75e382d5c0"}
                    },
                    "NewImage": {
                        "topic": {
                            "S": "https://daringfireball.net/feeds/main"
                        },
                        "id": {"S": "ac793191-c143-4762-90b7-cc75e382d5c0"},
                    },
                    "SequenceNumber": "100000000025935825479",
                    "SizeBytes": 118,
                    "StreamViewType": "NEW_IMAGE",
                },
                "eventSourceARN": "",
            },
        ]
    }
