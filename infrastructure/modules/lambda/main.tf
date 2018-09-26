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
  count = "${var.policies_count}"

  role       = "${aws_iam_role.main.name}"
  policy_arn = "${element(aws_iam_policy.main.*.arn, count.index)}"
}

resource "aws_iam_policy" "main" {
  count = "${var.policies_count}"

  name        = "${var.namespace}-lambda-${var.name}-policy-${count.index + 1}"
  description = "Managed by Terraform"

  policy = "${var.policies[count.index]}"
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
