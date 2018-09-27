data "archive_file" "verify" {
  type        = "zip"
  source_file = "../verify/app.py"
  output_path = "../verify/app.zip"
}

data "aws_iam_policy_document" "verify" {
  statement {
    sid = "TopicGetItem"

    actions = [
      "dynamodb:GetItem",
    ]

    effect    = "Allow"
    resources = ["${aws_dynamodb_table.topic.arn}"]
  }
}

module "lambda_verify" {
  source = "modules/lambda"

  namespace = "macnerd-hub"
  name      = "verify"
  filename  = "${data.archive_file.verify.output_path}"
  checksum  = "${data.archive_file.verify.output_base64sha256}"
  policies  = ["${data.aws_iam_policy_document.verify.json}"]

  # see https://github.com/hashicorp/terraform/issues/10857
  policies_count = 1
}

data "archive_file" "notification" {
  type        = "zip"
  source_file = "../notification/app.py"
  output_path = "../notification/app.zip"
}

data "aws_iam_policy_document" "notification" {
  statement {
    sid = "TopicGetItem"

    actions = [
      "dynamodb:GetItem",
    ]

    effect    = "Allow"
    resources = ["${aws_dynamodb_table.topic.arn}"]
  }

  statement {
    sid = "ItemBatchWriteItem"

    actions = [
      "dynamodb:BatchWriteItem",
    ]

    effect    = "Allow"
    resources = ["${aws_dynamodb_table.item.arn}"]
  }
}

module "lambda_notification" {
  source = "modules/lambda"

  namespace = "macnerd-hub"
  name      = "notification"
  filename  = "${data.archive_file.notification.output_path}"
  checksum  = "${data.archive_file.notification.output_base64sha256}"
  policies  = ["${data.aws_iam_policy_document.notification.json}"]

  # see https://github.com/hashicorp/terraform/issues/10857
  policies_count = 1
}
