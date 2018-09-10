#!/bin/bash

all:
	@echo "hello world"

package:
	aws cloudformation package \
		--template-file template.yaml \
		--s3-bucket pinub-deployments \
		--output-template-file packaged.yaml

deploy:
	aws cloudformation deploy \
		--template-file packaged.yaml \
		--stack-name pinub \
		--capabilities CAPABILITY_IAM
