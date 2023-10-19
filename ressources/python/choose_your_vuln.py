#!/usr/bin/env python3
from ressources.python.controller import * 
from ressources.python.functions import * 

def choose_your_vuln_env (choice) : 
    
    if choice == "windows" : 
        choice = "widows"
        vulns_list = WINDOWS_VULNS
        env = "windows"
        choose_your_vuln(env,vulns_list)
    elif choice == "linux" :
        vulns_list = LINUX_VULNS
        env = "linux"
        choose_your_vuln(env,vulns_list)
    else : 
        vulns_list = APPLICATIONS_VULNS
        env = "docker"
        choose_your_vuln(env,vulns_list)
        
def choose_your_vuln(env,vulns_list) :
    
    vuln_choice_num = ""
    while check_user_input(vuln_choice_num) == False : 
        i = 0
        print ("Select your vuln among the following list : \n")
        for vuln in vulns_list : 
            print (i," - "+vuln)
            i = i + 1 
        print ("b  - back")
        vuln_choice_num = input (" >> ")
        if vuln_choice_num == "b":
            return

    while True :
        vuln_choice_num = int(vuln_choice_num)
        if vuln_choice_num >= 0 and vuln_choice_num < len(vulns_list) :
            vuln_choice_str =  vulns_list[vuln_choice_num]
            if vuln_choice_str in vulns_list :
                print (bcolors.OKGREEN+"You have choosen "+vuln_choice_str+"."+bcolors.ENDC+" Please wait a few moment, during the building phase")
                input("Press Enter to continue...")
                if check_if_file_exist(env,vuln_choice_str) == "vagrant" : 
                    try: 
                        print (bcolors.OKGREEN+""+vuln_choice_str+""+bcolors.ENDC+" "+bcolors.OKCYAN+"is provided as a VM. she use vagrant to autoconfigure itself and virtualbox for emulating. "+bcolors.ENDC)
                        vagrant_file_path = env+"/"+vuln_choice_str
                        current_dir = os.getcwd()
                        full_path = current_dir+'/'+vagrant_file_path
                        print (full_path)
                        os.environ['VAGRANT_CWD'] = full_path
                        subprocess.call(['vagrant', 'up'])
                        print (bcolors.OKGREEN+"Your VM "+vuln_choice_str+" is ready."+bcolors.ENDC+" Check the "+env+"/"+vuln_choice_str+"/README.md for more information about your target")
                        if env == "linux" : 
                            ssh_or_not = input("VM has been instancied succefully ! Do you want to connect to it now (SSH) ? [y/N]" or "N")
                            if ssh_or_not == "Y" or ssh_or_not == "y" : 
                                subprocess.call(['bash', 'ressources/scripts/ssh.sh', full_path ])
                    except Exception as e: 
                        print(e)
                else : 
                    try : 
                        current_path =  os.path.abspath(os.getcwd())
                        print (bcolors.OKGREEN+""+vuln_choice_str+""+bcolors.ENDC+" "+bcolors.OKCYAN+" is provided as a container. (docker need root rights) "+bcolors.ENDC)
                        subprocess.call(['sudo', 'docker-compose', '-f', current_path+"/applications/"+vuln_choice_str+"/docker-compose.yml", "up", "-d" ])
                        print (bcolors.OKGREEN+"Your app "+vuln_choice_str+" is ready."+bcolors.ENDC+" Check the ./applications/"+vuln_choice_str+"/README.md and the \"docker lab manager\" root menu for more information about your target")
                    except Exception as e: 
                        print (e)
                    
            input("Press Enter to continue...")
            break
                    
        else : 
            print (bcolors.WARNING+"Wrong Choice !"+bcolors.ENDC)
            vuln_choice_num = input (" >> ")