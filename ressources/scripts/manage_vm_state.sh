#!/bin/bash 

function state ()

    if [[ $1 == "status" ]]; then 
        if [[ $(vboxmanage list runningvms) ]]; then 
            echo "********** Running spoonable VM(s) **********"
            echo 
            for upVM in $(vboxmanage list runningvms | grep spoonable | awk {'print $1'});do
                echo " - $upVM"
            done
            echo "**********************************************" 
            echo 
        else
            stopped_VMs=$(vboxmanage list vms | grep spoonable- | awk {'print $1'})
            if [ -z "$stopped_VMs" ]; then 
                echo "no VMs prefixed with spoonable-* existing"
            else
                echo "no VMs prefixed with spoonable-* are up, but vm(s) \"spoonabled\" existing : "
                for VM in $(vboxmanage list vms | grep spoonable- | awk {'print $1'});do
                    echo "$VM"
                done 
                echo "What do you want to do ?"
            fi
        fi
    elif [[ $1 == "start" ]]; then 
        for vm in $(vboxmanage list vms | grep spoonable- | awk {'print $2'}); do 
            VBoxManage startvm $vm --type headless
        done

    elif [[ $1 == "destroy" ]]; then 
        for vm in $(vboxmanage list vms | grep spoonable- | awk {'print $2'}); do 
            echo "$vm"
            vboxmanage unregistervm $vm --delete 
        done

    elif [[ $1 == "delete" ]]; then 
            _path="/home/$USER/.vagrant.d/boxes"
            path_size=$(du -sh $_path | awk {'print $1'})
            rm -rf $_path/*
            if [ -z "$(ls -A $_path)" ]; then
                echo "Vagrant lab images has been erased from the disk ($_path). You have freed up $path_size"
            else
                echo "An error has been occured during the delete process. please check the following folder : $_path"
            fi
    else 
        for vm in $(vboxmanage list runningvms | grep spoonable- | awk {'print $2'}); do 
            echo "$vm"
            vboxmanage controlvm $vm $1
        done
    fi

function is_kali_is_installed() {
    running_container=$(vboxmanage list vms | grep Kalilinux-spoonable | awk {'print $1'})
    if [ -z "$running_container" ]; then 
        echo "Kalilinux is not yet installed."
    fi
}
