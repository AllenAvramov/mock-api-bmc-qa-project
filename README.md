## How to run Docker with jenkins

docker run -d \
 --name jenkins \
 --user root \
 -p 8080:8080 \
 -p 50000:50000 \
 -v jenkins_home:/var/jenkins_home \
 -v /var/run/docker.sock:/var/run/docker.sock \  
 jenkins-with-docker

## Jenkins image with Docker CLI and mounted the Docker socket so Jenkins could run Docker commands in the pipeline.

FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y docker.io && rm -rf /var/lib/apt/lists/\*
USER jenkins

## How to run server

python3 -m uvicorn app.main:app --reload
