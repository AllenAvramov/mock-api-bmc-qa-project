pipeline {
    agent any 
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t mock-api .'
            }
        }
        stage('Run container'){
            steps {
                sh 'docker rm -f mock-api || true'
                sh 'docker run -d -p 8000:8000 --name mock-api mock-api'
                sh 'sleep 5' // important to give API time to start before running tests
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker exec mock-api pytest tests/'
            }
        }
        stage('DockerHub Login'){
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds', 
                    usernameVariable: 'DH_USER', 
                    passwordVariable: 'DH_PASS')]) {
                sh '''
                    echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin 
                ''' // | sends that output as input to the next command
                }
            }
        }
        stage('Push to DockerHub'){
            steps {
                sh '''
                docker tag mock-api allenavramov/mock-api:latest
                docker push allenavramov/mock-api:latest
                '''
            }
        }
        stage('Pull & Run from DockerHub') { //To validate that the image pushed to DockerHub is complete, runnable, and independent of the build environment.
            steps {
                sh '''
                    docker rm -f mock-api || true

                    docker rmi mock-api || true
                    docker rmi allenavramov/mock-api:latest || true

                    docker pull allenavramov/mock-api:latest
                    docker run -d -p 8000:8000 --name mock-api allenavramov/mock-api:latest
                '''
            }
        }
    }
    post { //runs After the pipeline finishes
        always {
            sh 'docker rm -f mock-api || true' // with no true, if there is no such a container, pipeline fails. with true it ignores the error
        }
    }
}