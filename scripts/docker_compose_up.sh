#!/bin/bash

cd /home/ec2-user/app

# Stop existing services
echo "Stopping existing services..."
docker-compose down

# Pull the latest image
echo "Pulling the latest Docker image..."
docker-compose pull --ignore-pull-failures --no-cache

# List available images (for debugging)
echo "Listing Docker images..."
docker images

# Start fresh
echo "Starting the application..."
docker-compose up -d

# Check running containers (for debugging)
echo "Running containers..."
docker ps
