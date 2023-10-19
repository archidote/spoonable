#!/bin/bash
function list() {
    echo "********** Running spoonable container(s) **********"
    running_containers=$(sudo docker ps --format {{.Names}} | grep spoonable)
    stopped_containers=$(sudo docker ps -a --format {{.Names}} | grep spoonable)
    if [ -z "$running_containers" ]; then 
        if [ -z "$stopped_containers" ]; then 
            echo "No containers are prefixed with spoonable are currently existing."
            echo 
        else 
            echo "Container(s) prefixed with spoonable exist, but they are currently stopped."
            echo  
            sudo docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.State}}\t{{.Ports}}" | grep 'exited' | grep 'spoonable'
        fi
    else 
        echo "Container(s) prefixed with spoonable is/are currently running :" 
        echo 
        sudo docker ps --format "table {{.ID}}\t{{.Names}}\t{{.State}}\t{{.Ports}}" | grep spoonable
    fi
    echo "****************************************************"
}

function action() {

    running_containers=$(sudo docker ps --format {{.Names}} | grep spoonable)
    if [ $1 == "rm" ]; then 
        sudo docker ps -aq --filter name="spoonable" | xargs sudo docker rm -f 
    elif [ $1 == "rmi" ]; then 
        sudo docker ps -q --filter name="spoonable" | xargs sudo docker kill 
        sudo docker ps -aq --filter name="spoonable" | xargs sudo docker rm -f 
        sudo docker images --format {{.ID}} "spoonable\/*" | xargs sudo docker rmi -f 
    elif [ $1 == "stop" ]; then 
        sudo docker ps -q --filter name="spoonable" | xargs sudo docker stop
    elif [ $1 == "start" ]; then 
        sudo docker ps -aq --filter name="spoonable" | xargs sudo docker start
    else
        sudo docker ps -q --filter name="spoonable" | xargs sudo docker kill 
    fi
}
