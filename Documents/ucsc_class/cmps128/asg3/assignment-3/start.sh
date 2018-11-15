docker build --tag assignment2 .
docker run -d --rm -p 8081:8080 --name master -e IP=0.0.0.0 -e PORT=8080 assignment2:latest
docker run -d --rm -p 8082:8080 --name slave-8082 -e IP=0.0.0.0 -e PORT=8080 -e MAINIP=127.0.0.1:8081 assignment2:latest
docker run -d --rm -p 8083:8080 --name slave-8083 -e IP=0.0.0.0 -e PORT=8080 -e MAINIP=127.0.0.1:8081 assignment2:latest
