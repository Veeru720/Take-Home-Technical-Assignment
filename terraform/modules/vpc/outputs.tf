output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "eks_security_group_id" {
  description = "Security group for EKS cluster"
  value       = aws_security_group.eks_sg.id
}
