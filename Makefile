#!/bin/bash

STACK_NAME ?= macnerd
NOW = $(shell date +%s)
TABLES = "${STACK_NAME}-topic" "${STACK_NAME}-item"

all:
	@echo "hello world"

backup:
	@for t in ${TABLES}; do \
		aws dynamodb create-backup --table-name $$t --backup-name $$t-${NOW}; \
	done

test:
	# only way to prevent creation of __pycache__ directories
	# https://stackoverflow.com/a/47893653/3833166
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider
