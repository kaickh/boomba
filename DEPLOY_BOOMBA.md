# Deploy OCT to boomba on AWS

Repo: https://github.com/kaickh/boomba

## Step 1: Push code to boomba

Code is committed locally. Push from your terminal (auth required):

```bash
cd /Users/kai/me/liberia/technology/oct

# If large push fails, increase buffer:
git config http.postBuffer 524288000

# Push (use SSH if you have keys: git@github.com:kaickh/boomba.git)
git push boomba dev:main
```

If push fails (HTTP 400, timeout): try SSH, or push in smaller chunks. The repo has full Paperless-ngx history (~11k commits).

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
