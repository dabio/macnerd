resource "aws_dynamodb_table" "topic" {
  name = "macnerd-topic"

  read_capacity  = 5
  write_capacity = 5
  hash_key       = "id"

  stream_enabled   = true
  stream_view_type = "NEW_IMAGE"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "item" {
  name = "macnerd-item"

  read_capacity  = 5
  write_capacity = 5
  hash_key       = "id"

  #  stream_enabled   = true
  #  stream_view_type = "NEW_IMAGE"

  attribute {
    name = "id"
    type = "S"
  }
}
