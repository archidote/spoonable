# sudo breakout 

## Technical Description 

*This system is vulnerable to a CVE released in 2022 (maybe other CVE impact the app version now).*

- **Context** : Post-Exploitation 
  
  - Enter into the targeted container shell
  - The goal here is to pwned (become root) completly the container.

## How to start your tests ? 

```
docker-compose up -d 
docker ps 
docker exec -it <id of the container> /bin/bash 
```