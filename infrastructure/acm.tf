provider "aws" {
  alias = "us-east-1"

  region = "us-east-1"
}

resource "aws_acm_certificate" "main" {
  provider = "aws.us-east-1"

  domain_name       = "${local.domain}"
  validation_method = "DNS"

  subject_alternative_names = ["*.${local.domain}"]
}

resource "aws_route53_record" "certificate_validation" {
  count = "${length(aws_acm_certificate.main.domain_validation_options)}"

  zone_id = "${aws_route53_zone.macnerd.id}"

  name = "${lookup(aws_acm_certificate.main.domain_validation_options[count.index], "resource_record_name")}"
  type = "${lookup(aws_acm_certificate.main.domain_validation_options[count.index], "resource_record_type")}"
  ttl  = "900"

  records = [
    "${lookup(aws_acm_certificate.main.domain_validation_options[count.index], "resource_record_value")}",
  ]
}

# doesn't work ¯\_(ツ)_/¯
#resource "aws_acm_certificate_validation" "main" {
#  count = "${length(aws_acm_certificate.main.domain_validation_options)}"
#
#  certificate_arn = "${aws_acm_certificate.main.arn}"
#
#  validation_record_fqdns = [
#    "${element(aws_route53_record.certificate_validation.*.fqdn, count.index)}",
#  ]
#}

