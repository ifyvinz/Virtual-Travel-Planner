#!/bin/bash

cd /home/ec2-user/app

# Stop existing services
docker-compose down

# Pull the latest image from Amazon ECR
docker-compose pull

# Start fresh
docker-compose up -d
