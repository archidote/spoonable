# Log 4 Ever

## Guidelines to exploit the vulnerability

*This app is vulnerable to a famous CVE released in 2021 (maybe others CVE impact the app version now).*

- **Context** : Exploitation & Post Exploitation 
  - No creds are required. 
  - The goal here is to pwned (become root) completly the server.

## How to reach it ? 

```
docker-compose up -d 
curl http://localhost:8083
```

