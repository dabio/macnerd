resource "aws_s3_bucket" "deployments" {
  bucket = "macnerd-deployments"

  tags {
    namespace = "macnerd"
  }
}
