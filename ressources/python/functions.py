#!/usr/bin/env python3
from os.path import exists
from ressources.python.controller import * 

def check_if_file_exist(env,vuln_choice) : 
    
    if env == "other" :
        file_type = "docker-compose.yml" 
    else : 
        file_type = "Vagrantfile"
        
    reconstruct_path = ""+env+"/"+vuln_choice+"/"+file_type+""
    if exists(reconstruct_path) == True : 
        print ("the file "+reconstruct_path+" exist")
        if env == "other" : 
            return "docker"
        else : 
            return "vagrant"
    
def check_user_input(user_input): 
    
    if user_input.isnumeric() : 
        return True
    elif user_input == "q": 
        up_or_not_before_exit()
        exit()
    else : 
        os.system('clear')
        return False 
    
def up_or_not_before_exit(): 
    print ("Checking if VMs/containers are running in the background...")
    vm = subprocess.call(['bash', '-c', 'vboxmanage list runningvms | grep "spoonable-*"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    container = subprocess.call(['bash', '-c', 'sudo docker ps | grep "spoonable-*"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if container == 0 : 
        are_you_sure = input ("Stop all containers with a prefixed name spoonable* ? [y/N]" or "N")
        if are_you_sure == "Y" or are_you_sure == "y" : 
            subprocess.call(['bash', '-c', '. ressources/scripts/manage_containers_state.sh; action stop'])
    if vm == 0 : 
        are_you_sure = input ("Stop all VM with a prefixed name spoonable* ? [y/N]" or "N") 
        if are_you_sure == "Y" or are_you_sure == "y" : 
            subprocess.call(['bash', '-c', '. ressources/scripts/manage_vm_state.sh; state poweroff'])
    print ("Exiting...")



