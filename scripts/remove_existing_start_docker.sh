#!/bin/bash
if [ -e /home/ec2-user/app/scripts/start_docker.sh ]; then
    sudo rm -rf /home/ec2-user/app/scripts/start_docker.sh
fi

if [ -e /home/ec2-user/app/scripts/docker_compose_up.sh ]; then
    sudo rm -rf /home/ec2-user/app/scripts/docker_compose_up.sh
fi
