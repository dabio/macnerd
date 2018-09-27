resource "aws_cognito_user_pool" "user" {
  name = "macnerd-users"

  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  password_policy {
    minimum_length    = 6
    require_lowercase = false
    require_numbers   = false
    require_symbols   = false
    require_uppercase = false
  }
}

resource "aws_cognito_user_pool_client" "user" {
  name = "macnerd.de"

  generate_secret     = true
  explicit_auth_flows = ["USER_PASSWORD_AUTH"]

  user_pool_id = "${aws_cognito_user_pool.user.id}"
}
