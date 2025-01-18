#!/bin/bash

# Navigate to the application directory
cd /home/ec2-user/app

# Ensure Docker Compose is using the latest images
docker-compose pull

# Start services with Docker Compose
docker-compose up -d
