# Helpdesk

## Guidelines to exploit the vulnerability

*This app is vulnerable to several CVE released in 2022 (maybe other CVE impact the app version now).*

Try to exploit one or more vulnerabilities. 

- **Context** : Exploitation & Post Exploitation 
  - No creds are required. 
  - The aim here is to obtain code execution on the server hosting the application via the user executing the web application.

## How to start your tests ? 

```
docker-compose up -d 
curl http://localhost:8082
```

