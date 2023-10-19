# Docker Registry misconfiguration

*This artifact is not a vulnerability per se but is the result of a common misconfiguration that results in a security flaw* 

### Context : Exploitation & Post-Exploitation
  - No creds are required. 
  - The goal here is to extract confidential (password, tokens, etc.) data from a docker image that is hosted in an insecure manner.

## How to reach the docker registry ? 

```
curl -I http://ip-of-the-docker-prv-registry:5000
```
