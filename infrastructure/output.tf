output "cognito client_id" {
  value = "${aws_cognito_user_pool_client.user.id}"
}

output "cognito client_secret" {
  value = "${aws_cognito_user_pool_client.user.client_secret}"
}
