variable "namespace" {
  type    = "string"
  default = "macnerd"
}

variable "name" {
  type = "string"
}

variable "policies" {
  type    = "list"
  default = []
}

variable "policies_count" {
  type    = "string"
  default = ""
}

variable "filename" {
  type = "string"
}

variable "checksum" {
  type = "string"
}
