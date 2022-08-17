#!/bin/bash

echo "FROM httpd:latest" > Dockerfile
echo "COPY files/index.html /usr/local/apache2/htdocs/" >> Dockerfile
echo "EXPOSE 80" >> Dockerfile


docker build -t apachedocker2 .
docker run -it -d -p 8088:80 apachedocker2
