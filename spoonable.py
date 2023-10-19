#!/usr/bin/env python3
from ressources.python.functions import * 
from ressources.python.labs_manager import * 
from ressources.python.choose_your_vuln import * 

def main () :
    while True : 
        choice_num = ""
        while check_user_input(choice_num) == False : 
            print ("""
                                    _     _      
                                   | |   | |     
  ___ _ __   ___   ___  _ __   __ _| |__ | | ___ 
 / __| '_ \ / _ \ / _ \| '_ \ / _` | '_ \| |/ _ \\
 \__ \ |_) | (_) | (_) | | | | (_| | |_) | |  __/
 |___/ .__/ \___/ \___/|_| |_|\__,_|_.__/|_|\___|
     | |                                         
     |_|                                         

Pentesting environment "On premise" for a workstation - github.com/archidote

            """)
            print ("Select an option :")
            i = 0 
            for item in ROOT_MENU : 
                print (i," - "+item)
                i = i + 1 
            print ("q  - quit")
            choice_num = input (" >> ")
        if int(choice_num) >= 0 and int(choice_num) < len(ROOT_MENU) : 
            choice_str = ROOT_MENU[int(choice_num)]
            if choice_str in ROOT_MENU :
                if choice_str == "linux" or choice_str == "applications" or choice_str == "windows": 
                    choose_your_vuln_env(choice_str)
                elif choice_str == "Vagrant lab manager" : 
                    vagrant_lab_manager() 
                elif choice_str == "Docker container lab manager" : 
                    docker_lab_manager()
                elif choice_str == "Install/Launch Kali" : 
                    install_or_launch_kali()    
                else :
                    os.system('clear')
                    print ("To update spoonable, exit the program and run the following commands: git pull ")
                    input("Press Enter to continue...")        
                    
if __name__ == '__main__':
    for program in REQUIRED_PROGRAMES : 
        if os.path.isfile("/usr/bin/"+program) != True :
            raise Exception(bcolors.FAIL+"Error :"+bcolors.ENDC+" "+program+" is not installed. Please check the doc to install in a convenient way.")
    main()