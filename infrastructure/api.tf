resource "aws_api_gateway_rest_api" "hub" {
  name = "macnerd-hub"

  endpoint_configuration {
    types = ["${local.type}"]
  }
}

resource "aws_api_gateway_stage" "prod" {
  rest_api_id   = "${aws_api_gateway_rest_api.hub.id}"
  stage_name    = "${local.stage_name}"
  deployment_id = "${aws_api_gateway_deployment.prod.id}"

  xray_tracing_enabled = true
}

resource "aws_api_gateway_deployment" "prod" {
  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  stage_name  = "${local.stage_name}"

  depends_on = [
    "aws_api_gateway_integration.verify",
    "aws_api_gateway_integration.notification",
  ]
}

resource "aws_api_gateway_domain_name" "hub" {
  domain_name = "hub.${local.domain}"

  certificate_arn = "${aws_acm_certificate.main.arn}"

  endpoint_configuration {
    types = ["${local.type}"]
  }
}

resource "aws_api_gateway_base_path_mapping" "hub" {
  api_id      = "${aws_api_gateway_rest_api.hub.id}"
  stage_name  = "${aws_api_gateway_stage.prod.stage_name}"
  domain_name = "${aws_api_gateway_domain_name.hub.domain_name}"
}

resource "aws_api_gateway_resource" "topic" {
  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  parent_id   = "${aws_api_gateway_rest_api.hub.root_resource_id}"

  path_part = "{id}"
}

# verify

resource "aws_api_gateway_method" "verify" {
  http_method   = "GET"
  authorization = "NONE"

  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  resource_id = "${aws_api_gateway_resource.topic.id}"
}

resource "aws_api_gateway_integration" "verify" {
  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  resource_id = "${aws_api_gateway_resource.topic.id}"
  http_method = "${aws_api_gateway_method.verify.http_method}"

  type = "AWS_PROXY"
  uri  = "${module.lambda_verify.invoke_arn}"

  integration_http_method = "POST"
}

resource "aws_lambda_permission" "verify" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = "${module.lambda_verify.function_name}"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_stage.prod.execution_arn}/${aws_api_gateway_method.verify.http_method}${aws_api_gateway_resource.topic.path}"
}

# notification

resource "aws_api_gateway_method" "notification" {
  http_method   = "POST"
  authorization = "NONE"

  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  resource_id = "${aws_api_gateway_resource.topic.id}"
}

resource "aws_api_gateway_integration" "notification" {
  rest_api_id = "${aws_api_gateway_rest_api.hub.id}"
  resource_id = "${aws_api_gateway_resource.topic.id}"
  http_method = "${aws_api_gateway_method.notification.http_method}"

  type = "AWS_PROXY"
  uri  = "${module.lambda_notification.invoke_arn}"

  integration_http_method = "POST"
}

resource "aws_lambda_permission" "notification" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = "${module.lambda_notification.function_name}"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_stage.prod.execution_arn}/${aws_api_gateway_method.notification.http_method}${aws_api_gateway_resource.topic.path}"
}
