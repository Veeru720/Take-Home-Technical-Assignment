# VPC module first
module "vpc" {
  source               = "./modules/vpc"
  cidr_block           = "10.0.0.0/16"
  private_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
  availability_zones   = ["us-east-1a", "us-east-1b"]
}

# IAM assume role policy for EKS
data "aws_iam_policy_document" "eks_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }
  }
}

# EKS module AFTER VPC and IAM policy exist
module "eks" {
  source       = "./modules/eks"
  cluster_name = var.cluster_name
  role_arn     = var.role_arn
  policy       = data.aws_iam_policy_document.eks_assume_role.json

  subnet_ids         = module.vpc.private_subnet_ids
  security_group_ids = [module.vpc.eks_security_group_id]
}
