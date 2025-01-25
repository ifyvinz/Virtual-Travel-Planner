#!/bin/bash

cd /home/ec2-user/app

# Login to AWS ECR 
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com

# Stop existing services
echo "Stopping existing services..."
docker-compose down
docker rm -f $(docker ps -q -a)
docker rmi -f $(docker images -q)

# Pull the latest Docker image
echo "Pulling the latest Docker image..."
docker-compose pull --ignore-pull-failures --no-cache

# Start fresh
echo "Starting the application..."
docker-compose up -d

# Check running containers
echo "Running containers..."
docker ps
