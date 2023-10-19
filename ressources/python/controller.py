#!/usr/bin/env python3
import os, subprocess, time 
from ressources.python.functions import * 
from ressources.python.colors import * 

ROOT_MENU = ["linux", "applications" , "windows", "Vagrant lab manager", "Docker container lab manager", "Install/Launch Kali", "Update"]
REQUIRED_PROGRAMES = ["virtualbox", "vagrant", "ansible", "docker", "docker-compose"]
LINUX_VULNS = sorted(os.listdir("linux/")) ; 
APPLICATIONS_VULNS = sorted(os.listdir("applications/"))
WINDOWS_VULNS = sorted(os.listdir("windows/")) 
