locals {
  runtime     = "python3.6"
  handler     = "app.handler"
  memory_size = "128"
}

resource "aws_lambda_function" "main" {
  filename         = "${var.filename}"
  function_name    = "${var.namespace}-${var.name}"
  source_code_hash = "${var.checksum}"

  runtime     = "${local.runtime}"
  handler     = "${local.handler}"
  memory_size = "${local.memory_size}"

  role = "${aws_iam_role.main.arn}"

  tracing_config {
    mode = "Active"
  }
}

resource "aws_iam_role" "main" {
  name        = "${var.namespace}-lambda-${var.name}"
  description = "Managed by Terrafrom"

  assume_role_policy = "${data.aws_iam_policy_document.assume.json}"
}

resource "aws_iam_role_policy_attachment" "logs" {
  role       = "${aws_iam_role.main.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "xray" {
  role       = "${aws_iam_role.main.name}"
  policy_arn = "arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess"
}

resource "aws_iam_role_policy_attachment" "custom" {
  count = "${length(var.policy) > 0 ? 1 : 0}"

  role       = "${aws_iam_role.main.name}"
  policy_arn = "${aws_iam_policy.main.arn}"
}

resource "aws_iam_policy" "main" {
  count = "${length(var.policy) > 0 ? 1 : 0}"

  name        = "${var.namespace}-lambda-${var.name}-policy"
  description = "Managed by Terraform"

  policy = "${var.policy}"
}

data "aws_iam_policy_document" "assume" {
  statement {
    sid = "AssumeRole"

    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}
