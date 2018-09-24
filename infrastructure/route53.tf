resource "aws_route53_zone" "macnerd" {
  name = "${local.domain}"
}
