# Deploy OCT to boomba on AWS

Repo: https://github.com/kaickh/boomba

## Step 1: Push code to boomba

```bash
cd /Users/kai/me/liberia/technology/oct

# Add boomba as remote (if not already)
git remote add boomba https://github.com/kaickh/boomba.git

# Stage OCT changes
git add .cursor/ .github/workflows/deploy-aws.yml AGENTS.md DEPLOY_AWS.md OCT_README.md QUICKSTART.md docker-compose.aws.yml docker-compose.oct.yml infra/ paperless.conf.dev src/oct/
git add -u  # modified files

# Commit
git commit -m "OCT: platform extensions, AWS deploy, Cursor rules"

# Push to boomba (main or dev)
git push boomba dev:main
# Or if boomba has no branches yet:
git push boomba HEAD:main
```

## Step 2: Create ECR in AWS

```bash
cd infra/terraform
terraform init
terraform apply -auto-approve
```

Note the `ecr_repository_url` output.

## Step 3: Add GitHub secrets to boomba

Go to https://github.com/kaickh/boomba/settings/secrets/actions

Add:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g. `us-east-1`)

## Step 4: Trigger build

Push triggers the workflow. Or: Actions → Build and Push to ECR → Run workflow.

Build runs ~15–25 min. Image lands in ECR.

## Step 5: Deploy

Use the image from ECR on EC2 or ECS. See DEPLOY_AWS.md.
