#!/bin/bash
function ssh() {
    echo "Loading..."
    cd "$1";
    vagrant ssh 
}
ssh $1