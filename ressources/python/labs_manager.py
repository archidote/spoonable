#!/usr/bin/env python3
from ressources.python.controller import * 
from ressources.python.functions import * 

def vagrant_lab_manager(): 
    
    choice_num = ""
    vm_state = ["start", "poweroff", "reset", "pause", "savestate", "destroy", "delete"]
    
    while check_user_input(choice_num) != True: 
        i = 0 
        subprocess.call(['bash', '-c', '. ressources/scripts/manage_vm_state.sh; state status'])
        for state in vm_state : 
            print (str(i)+". "+state)
            i = i + 1 
        print ("b. back")
        choice_num = input (" >> ")
        if choice_num == "b":
            return
    
    choice_num = int(choice_num)
    if choice_num >= 0 and choice_num < len(vm_state) :
        choice_str = vm_state[int(choice_num)]
        if choice_str in vm_state :
            are_you_sure = input (bcolors.WARNING+"WARNING !"+bcolors.ENDC+" This action will "+choice_str+" all spoonable VM. Are you sure ? [y/N]" or "N")
            if are_you_sure == "Y" or are_you_sure == "y" : 
                subprocess.call(['bash', '-c', '. ressources/scripts/manage_vm_state.sh; state '+choice_str+''])
            else : 
                check_user_input("clear")
                print (bcolors.WARNING+"Process have been canceled."+bcolors.ENDC+"")
                time.sleep(2)
    input("Press Enter to continue...")
                

        
def docker_lab_manager(): 
    
    choice_num = ""
    containers_state = [ "start", "stop", "kill", "rm", "rmi" ] 

    while check_user_input(choice_num) != True : 
        i = 0 
        subprocess.call(['bash', '-c', '. ressources/scripts/manage_containers_state.sh; list'])
        for container in containers_state : 
            print (str(i)+". "+container)
            i = i + 1 
        print ("b. back")
        choice_num = input (" >> ")
        if choice_num == "b":
            return
        
    choice_num = int(choice_num)
    if choice_num >= 0 and choice_num < len(containers_state) :
        choice_str = containers_state[int(choice_num)]
        if choice_str in containers_state :
            are_you_sure = input (bcolors.WARNING+"WARNING !"+bcolors.ENDC+" This action will "+choice_str+" all lab's container which are prefixed with spoonable-*. Are you sure ? [y/N]" or "N")
            if are_you_sure == "Y" or are_you_sure == "y" : 
                subprocess.call(['bash', '-c', '. ressources/scripts/manage_containers_state.sh; action '+choice_str+''])
            else : 
                check_user_input("clear")
                print (bcolors.WARNING+"Process have been canceled."+bcolors.ENDC+"")
                time.sleep(2)
                docker_lab_manager()
        
        input("Press Enter to continue...")

def install_or_launch_kali(): 
    check_if_kali_exist = subprocess.run(['bash', '-c', '. ressources/scripts/manage_vm_state.sh; is_kali_is_installed '], capture_output=True).stdout.decode()
    if check_if_kali_exist != "": 
        check_user_input("clear")
        print (check_if_kali_exist)
        are_you_sure = input (bcolors.WARNING+"WARNING ! "+bcolors.ENDC+" you are about to download the latest version of Kalilinux (5go ~). Are you sure ? [y/N] " or "N")
        if are_you_sure == "Y" or are_you_sure == "y" : 
            try: 
                current_dir = os.getcwd()
                os.environ['VAGRANT_CWD'] = current_dir+'/ressources/kali/'
                subprocess.call(['vagrant', 'up'])
                print (bcolors.OKGREEN+"Good new !"+bcolors.ENDC+" Kalilinux is ready. check the ./ressources/kali/README.md for more information.")
            except Exception as e :
                print (e)
            input("Press Enter to continue...")
    else : 
        print (bcolors.OKGREEN+"Kalilinux is already installed ! "+bcolors.ENDC+" Check Virtual box GUI and start your tests ;-)")
        input("Press Enter to continue...")