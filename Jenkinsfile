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
                sh 'docker run -d -p 8000:8000 --name mock-api mock-api'
                sh 'sleep 5'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker exec mock-api pytest -q tests/'
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
    }
    post { //runs After the pipeline finishes
        always {
            sh 'docker rm -f mock-api || true' // with no true, if there is no such a container, pipeline fails. with true it ignores the error
        }
    }
}