# Docker Breakout

## Guidelines to exploit the vulnerability

*This artifact is not a software vulnerability per se but is the result of a human misconfiguration that results in a security flaw* 

- **Context** : Post-Exploitation
  - Enter into the targeted container shell
  - The goal here is to pwned the docker host (Become root on the host)

## How to start your tests ? 

```
docker-compose up -d 
docker ps 
docker exec -it <id of the container> /bin/bash 
```

