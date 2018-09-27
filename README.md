# macnerd

[![Build Status](https://semaphoreci.com/api/v1/dabio/macnerd/branches/master/badge.svg)](https://semaphoreci.com/dabio/macnerd)

A simple news feed aggregator. Uses superfeedr.

## Requirements

* `brew install terrafrom`
* `pip3 install --user awscli boto3`

## Commands

* `make backup`
  Create a backup of the dynamodb tables.
* `make deploy`
  Pushes everything live.

## Tests

`make test`

## Destroy Everything

This step is irreversible.

`make destroy`
