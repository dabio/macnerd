import pytest
from verify import app


CHALLENGE = 'olnkk73345qmdmhlrf6r'


def test_lambda_handler(apigw_event):
    ret = app.handler(apigw_event, "")
    assert ret["statusCode"] == 200
    assert ret["body"] == CHALLENGE


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "resource": "/topic/{id}",
        "path": "/topic/0019504b-4f69-4ec2-a43e-6eac2537c71d",
        "httpMethod": "GET",
        "headers": {
            "Accept-Encoding": "gzip, deflate",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "False",
            "CloudFront-Is-SmartTV-Viewer": "False",
            "CloudFront-Is-Tablet-Viewer": "False",
            "CloudFront-Viewer-Country": "US",
            "Host": "test1234.execute-api.eu-west-1.amazonaws.com",
            "User-Agent": "Superfeedr bot/2.0 http://superfeedr.com",
            "Via": "1.1 056e8663365bf1daf840591db57b77b6.cloudfront.net",
            "X-Amz-Cf-Id": "4d_8R-dfdsfd==",
            "X-Amzn-Trace-Id": "Root=1-5ba0b84a-fe3cea0060088fdc7570f446",
            "X-Forwarded-For": "198.58.102.96, 52.46.21.72",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "multiValueHeaders": {
            "Accept-Encoding": [
                "gzip, deflate"
            ],
            "CloudFront-Forwarded-Proto": [
                "https"
            ],
            "CloudFront-Is-Desktop-Viewer": [
                "true"
            ],
            "CloudFront-Is-Mobile-Viewer": [
                "False"
            ],
            "CloudFront-Is-SmartTV-Viewer": [
                "False"
            ],
            "CloudFront-Is-Tablet-Viewer": [
                "False"
            ],
            "CloudFront-Viewer-Country": [
                "US"
            ],
            "Host": [
                "test1234.execute-api.eu-west-1.amazonaws.com"
            ],
            "User-Agent": [
                "Superfeedr bot/2.0 http://superfeedr.com"
            ],
            "Via": [
                "1.1 056e8663365bf1daf840591db57b77b6.cloudfront.net"
            ],
            "X-Amz-Cf-Id": [
                "4d_8R-dfdsfd=="
            ],
            "X-Amzn-Trace-Id": [
                "Root=1-5ba0b84a-fe3cea0060088fdc7570f446"
            ],
            "X-Forwarded-For": [
                "198.58.102.96, 52.46.21.72"
            ],
            "X-Forwarded-Port": [
                "443"
            ],
            "X-Forwarded-Proto": [
                "https"
            ]
        },
        "queryStringParameters": {
            "hub.challenge": CHALLENGE,
            "hub.lease_seconds": "315360000",
            "hub.mode": "subscribe",
            "hub.topic": "https://daringfireball.net/feeds/main"
        },
        "multiValueQueryStringParameters": {
            "hub.challenge": [
                CHALLENGE
            ],
            "hub.lease_seconds": [
                "315360000"
            ],
            "hub.mode": [
                "subscribe"
            ],
            "hub.topic": [
                "https://daringfireball.net/feeds/main"
            ]
        },
        "pathParameters": {
            "id": "0019504b-4f69-4ec2-a43e-6eac2537c71d"
        },
        "stageVariables": "None",
        "requestContext": {
            "resourceId": "flx4in",
            "resourcePath": "/topic/{id}",
            "httpMethod": "GET",
            "extendedRequestId": "NaG7oG1AjoEFgTQ=",
            "requestTime": "18/Sep/2018:08:33:14 +0000",
            "path": "/Prod/topic/94deac4e-7887-4986-ae7f-a24db8051591",
            "accountId": "200885815221",
            "protocol": "HTTP/1.1",
            "stage": "Prod",
            "requestTimeEpoch": 1537259594407,
            "requestId": "7c06dbd9-bb1d-11e8-99b1-cb67dd6d12de",
            "identity": {
                "cognitoIdentityPoolId": "None",
                "accountId": "None",
                "cognitoIdentityId": "None",
                "caller": "None",
                "sourceIp": "198.58.102.96",
                "accessKey": "None",
                "cognitoAuthenticationType": "None",
                "cognitoAuthenticationProvider": "None",
                "userArn": "None",
                "userAgent": "Superfeedr bot/2.0 http://superfeedr.com",
                "user": "None"
            },
            "apiId": "auyek5vk39"
        },
        "body": "None",
        "isBase64Encoded": "False"
    }
