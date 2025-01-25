#!/bin/bash

cd /home/ec2-user/app

# Pull the latest code from the repository
#echo "Pulling the latest code from the repository..."
#git reset --hard  # Reset any local changes
#git pull origin main  # Update to the latest code 

# Stop existing services
echo "Stopping existing services..."
docker-compose down

# Pull the latest Docker image
echo "Pulling the latest Docker image..."
docker-compose pull --ignore-pull-failures --no-cache

# Start fresh
echo "Starting the application..."
docker-compose up -d

# Check running containers
echo "Running containers..."
docker ps
