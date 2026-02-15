# Deploy OCT on AWS

**No local Docker build.** Build runs in GitHub Actions (~15–25 min). You deploy from ECR.

---

## Quick path (3 steps)

### 1. Create ECR and get URL

```bash
cd infra/terraform
terraform init
terraform apply -auto-approve
terraform output ecr_repository_url
```

### 2. Add GitHub secrets

In your repo: Settings → Secrets → Actions. Add:

| Secret | Value |
|--------|-------|
| `AWS_ACCESS_KEY_ID` | Your AWS access key |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key |
| `AWS_REGION` | e.g. `us-east-1` |

### 3. Push to trigger build

```bash
git add .
git commit -m "Add AWS deploy"
git push origin dev
```

GitHub Actions builds the image and pushes to ECR. Check the Actions tab.

---

## Deploy the image

### Option A: EC2 (simplest)

1. Launch an EC2 (e.g. t3.medium, Amazon Linux 2023).
2. Install Docker, Docker Compose.
3. Create RDS PostgreSQL and ElastiCache Redis (or use the Terraform in `infra/terraform/ecs/` to create them).
4. Configure env vars and run:

```bash
# On EC2, after configuring AWS CLI
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY

export ECR_IMAGE=$ECR_REGISTRY/oct-paperless:latest
export PAPERLESS_DBHOST=your-rds-endpoint
export PAPERLESS_DBPASS=your-db-password
export PAPERLESS_REDIS=redis://your-elasticache-endpoint:6379

docker compose -f docker-compose.aws.yml up -d
```

### Option B: ECS Fargate

Use the Terraform in `infra/terraform/` (expand with ECS, RDS, ElastiCache). Or use AWS Copilot / App Runner for a managed deploy.

---

## Build without GitHub

To build and push from your machine (e.g. on a fast EC2):

```bash
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
docker build -t $ECR_REGISTRY/oct-paperless:latest .
docker push $ECR_REGISTRY/oct-paperless:latest
```
