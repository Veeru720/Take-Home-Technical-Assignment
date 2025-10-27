variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
}

variable "role_arn" {
  description = "IAM role ARN for EKS control plane"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for the EKS cluster"
  type        = list(string)
}

variable "security_group_ids" {
  description = "List of security group IDs for the EKS cluster"
  type        = list(string)
}

variable "policy" {
  description = "IAM assume role policy JSON for EKS"
  type        = string
}

variable "role_name" {
  description = "Name of the IAM role for EKS"
  type        = string
  default     = "eks-role"  
}
