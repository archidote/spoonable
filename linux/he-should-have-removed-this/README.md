# He should have removed this

*This artifact is not a vulnerability per se but is the result of a common misconfiguration that results in a security flaw* 

### Context : Post Exploitation

You have succeeded in obtaining a valide private key file and user in a insecure file. Find a way to elevate your privileges. 

- Use SSH to connect to the VM (Find it's IP first ;-) 

```
ssh -i /home/$USER/.vagrant.d/insecure_private_key spoonable@target-ip
```
- **Goal** : Promote yourself as root from spoonable user 