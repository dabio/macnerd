resource "aws_route53_zone" "macnerd" {
  name = "${local.domain}"
}

#resource "aws_route53_record" "hub" {
#  zone_id = "${aws_route53_zone.macnerd.id}"
#
#  name = "${aws_api_gateway_domain_name.hub.domain_name}"
#  type = "A"
#
#  alias {
#    name                   = "${aws_api_gateway_domain_name.hub.cloudfront_domain_name}"
#    zone_id                = "${aws_api_gateway_domain_name.hub.cloudfront_zone_id}"
#    evaluate_target_health = false
#  }
#}

