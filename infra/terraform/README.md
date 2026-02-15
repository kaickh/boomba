# OCT AWS Deployment

## Fast path: Build in CI, deploy to AWS

**No local Docker build.** Push to GitHub → CI builds → image in ECR.

### 1. Create ECR (one-time)

```bash
cd infra/terraform
terraform init
terraform apply
```

Note the `ecr_repository_url` output.

### 2. Configure GitHub Actions

Add repository secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (optional, defaults to us-east-1)

### 3. Push to trigger build

```bash
git push origin dev
```

GitHub Actions builds the image and pushes to ECR. Build runs on GitHub's runners (~15–25 min first time, faster with cache).

### 4. Deploy to ECS (or EC2)

Use the image from ECR. See `infra/ecs/` for ECS Fargate setup, or run on EC2:

```bash
# EC2: pull and run
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URL
docker pull $ECR_URL/oct-paperless:latest
docker compose -f docker-compose.aws.yml up -d
```

## Alternative: Build locally and push to ECR

If you prefer to build locally (e.g. on a fast machine):

```bash
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker build -t $ECR_URL/oct-paperless:latest .
docker push $ECR_URL/oct-paperless:latest
```
