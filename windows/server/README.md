# Backup server

## Guidelines to exploit the vulnerability

*This artifact is not a vulnerability per se but is the result of a common misconfiguration that results in a security flaw* 

## Technical Description 


- ** 1st Context** : Exploitation 
  - The main aim here is to steal the files (Hives files) used to manage LOCAL authentication on this machine, without using a login to connect to the machine. 

- ** 2nd Context** : Post Exploitation 
  - You've managed to obtain credentials by consulting various company resources. Will this machine lead you to pwned the spoonable.local domain ? 
      - creds : 
        - account : backup-srv-local-adm
        - password : backup123!

