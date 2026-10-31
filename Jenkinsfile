pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t flask-api .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
                sh 'docker run --rm -v "$PWD:/app" -w /app python:3.14-slim sh -c "pip install -r requirements.txt && pip install pytest && pytest -v"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application'
                sh 'docker rm -f flask-cicd || true'
                sh 'docker run -d --name flask-cicd -p 8083:5000 flask-api'
            }
        }
    }
}