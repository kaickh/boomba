# OCT - AWS deployment
# Run: terraform init && terraform plan && terraform apply

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# ECR repository for OCT image
resource "aws_ecr_repository" "oct" {
  name                 = "oct-paperless"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

# Output ECR URL for docker push / ECS
output "ecr_repository_url" {
  value = aws_ecr_repository.oct.repository_url
}

output "ecr_repository_name" {
  value = aws_ecr_repository.oct.name
}
