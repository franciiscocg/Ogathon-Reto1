Para iniciar contenedor docker
```
docker build -t ogathon-challenges-api -f Dockerfile .
docker run -d -p 8080:8080 --env ASPNETCORE_HTTP_PORTS=8080 --name ogathon-challenges-api ogathon-challenges-api
```
