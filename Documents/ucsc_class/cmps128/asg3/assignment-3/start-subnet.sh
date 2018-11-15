docker build --tag assignment2 .
docker run -d --rm -p 8081:8080 --net=mynet --ip=10.0.0.20 -e IP=10.0.0.20 -e PORT=8080 --name master assignment2:latest
docker run -d --rm -p 8082:8080 --net=mynet --ip=10.0.0.21 -e IP=10.0.0.21 -e PORT=8080 --name slave-8082 -e MAINIP=127.0.0.1:8080 assignment2:latest
docker run -d --rm -p 8083:8080 --net=mynet --ip=10.0.0.22 -e IP=10.0.0.22 -e PORT=8080 --name slave-8083 -e MAINIP=127.0.0.1:8080 assignment2:latest
docker run -d --rm -p 8084:8080 --net=mynet --ip=10.0.0.23 -e IP=10.0.0.23 -e PORT=8080 --name slave-8084 -e MAINIP=127.0.0.1:8080 assignment2:latest