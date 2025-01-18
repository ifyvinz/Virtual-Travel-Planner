#!/bin/bash

cd /home/ec2-user/app

# Stop existing services
docker-compose down

# Start fresh
docker-compose up -d
