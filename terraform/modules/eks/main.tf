resource "aws_eks_cluster" "my_eks_cluster" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_role.arn
  version  = "1.30"  # optional

  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
  }

  tags = {
    Environment = "dev"
  }
}
