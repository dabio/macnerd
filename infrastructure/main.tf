terraform {
  backend "s3" {
    bucket = "tf-infra"
    region = "eu-central-1"
    key    = "pinub-aws.tfstate"
  }
}
