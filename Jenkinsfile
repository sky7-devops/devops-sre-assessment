pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r app/requirements.txt
                    .venv/bin/python -m pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-sre-api .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down
                    docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 10
                    curl -f http://localhost/health
                '''
            }
        }
    }
}