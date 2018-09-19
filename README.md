# Serverless Application Model Test (SAM Test)

A test application using [AWS SAM](https://github.com/awslabs/serverless-application-model).

## Requirements

* `pip3 install --user awscli`

## Commands

* `make package`
  Creates the CloudFormation Stack yaml file.
* `make deploy`
  Pushes the CloudFormation Stack live.
* `make clean`
  Deletes fragments on S3 bucket.

## Tests

`make test`

## Destroy Everything

This step is irreversible.

`make destroy`
