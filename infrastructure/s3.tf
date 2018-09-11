resource "aws_s3_bucket" "deployments" {
  bucket = "pinub-deployments"

  tags {
    namespace = "pinub"
  }
}
