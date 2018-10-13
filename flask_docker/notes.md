
source 

https://medium.com/@ssola/building-microservices-with-python-part-2-9f951199094a


## install docker compose and test pip requirements

`sudo apt install docker-compose`

after that I ran into a problem restarting docker, 

this post helped me:

https://www.artificialworlds.net/blog/2015/07/17/docker-fails-to-start-on-ubuntu-15-04/

```
sudo systemctl unmask docker.service
sudo systemctl unmask docker.socket
sudo systemctl start docker.service
```

follow the source article to define:

- requirements.txt
- Dockerfile
- docker-compose.yml

to test pip requirements, use a temp container with pip

`docker run -t -i python:3 /bin/bash`

NOTE:

- alpine tag means this container image is built with alpine-linux (
extremely small, with built-in busybox)

- search for common images on Docker-Hub: https://hub.docker.com

run:

`pip install -r ./requirements.txt`

any installed package will be lost after logging out of this shell

to test the dockerfile and compose configuration:

`docker-compose up -d`

NOTE:

- do not change this: `version: 2` 

- the default value of environment, depends_on is []


