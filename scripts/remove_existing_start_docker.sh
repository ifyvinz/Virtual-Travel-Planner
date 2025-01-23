#!/bin/bash

# Check if start_docker.sh exists and is a directory, then remove it
if [ -d /home/ec2-user/app/scripts/start_docker.sh ]; then
    sudo rm -rf /home/ec2-user/app/scripts/start_docker.sh
elif [ -f /home/ec2-user/app/scripts/start_docker.sh ]; then
    sudo rm -f /home/ec2-user/app/scripts/start_docker.sh
fi

# Check if docker_compose_up.sh exists and is a directory, then remove it
if [ -d /home/ec2-user/app/scripts/docker_compose_up.sh ]; then
    sudo rm -rf /home/ec2-user/app/scripts/docker_compose_up.sh
elif [ -f /home/ec2-user/app/scripts/docker_compose_up.sh ]; then
    sudo rm -f /home/ec2-user/app/scripts/docker_compose_up.sh
fi
