#!/bin/bash

STACK_NAME ?= pinub
S3_BUCKET ?= ${STACK_NAME}-deployments
TEMPLATE_FILE ?= template.yaml
OUTPUT_TEMPLATE_FILE ?= packaged-${TEMPLATE_FILE}

all:
	@echo "hello world"

package:
	aws cloudformation package \
		--template-file ${TEMPLATE_FILE} \
		--s3-bucket ${S3_BUCKET} \
		--output-template-file ${OUTPUT_TEMPLATE_FILE}

deploy:
	aws cloudformation deploy \
		--template-file ${OUTPUT_TEMPLATE_FILE} \
		--stack-name ${STACK_NAME} \
		--capabilities CAPABILITY_IAM

clean:
	aws s3 rm --recursive s3://${S3_BUCKET}/
