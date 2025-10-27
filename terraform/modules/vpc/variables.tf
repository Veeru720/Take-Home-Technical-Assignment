variable "cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "private_subnet_cidrs" {
  description = "List of private subnet CIDRs"
  type        = list(string)
}

variable "availability_zones" {
  description = "List of availability zones for subnets"
  type        = list(string)
}
