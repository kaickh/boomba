---
name: aws-deployment
description: Deploy OCT services to AWS with production-grade patterns. Use when deploying, setting up infrastructure, configuring Lambda, S3, API Gateway, or CI/CD for AWS.
---

# AWS Deployment

## Deployment Principles

- **Infrastructure as Code**: Terraform, CDK, or CloudFormation—never manual
- **Environments**: dev, staging, prod with clear separation
- **Secrets**: AWS Secrets Manager or Parameter Store; never in code

## OCR Service Topology

```
[API Gateway] → [Lambda: API] → [SQS] → [Lambda: OCR Worker]
                    ↓                        ↓
              [DynamoDB/RDS]            [S3 Documents]
                    ↓                        ↓
              [S3: Results]  ←──────────────┘
```

## CI/CD

- Build → Test → Deploy (no deploy without passing tests)
- Use AWS CodePipeline, GitHub Actions, or similar
- Deploy to dev on merge; prod requires approval

## Commands (examples)

```bash
# Deploy infrastructure
cdk deploy --all --require-approval never  # dev
cdk deploy OctProd --require-approval broadening  # prod

# Run tests before deploy
npm run test && npm run deploy
```
