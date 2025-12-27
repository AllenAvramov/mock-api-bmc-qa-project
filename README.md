## How to run Docker with jenkins

docker run -d \
 --name jenkins \
 --user root \
 -p 8080:8080 \
 -p 50000:50000 \
 -v jenkins_home:/var/jenkins_home \
 -v /var/run/docker.sock:/var/run/docker.sock \  
 jenkins-with-docker

## How to run server

python3 -m uvicorn app.main:app --reload
