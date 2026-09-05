pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

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
                sh '''
                    docker build -t devops-sre-api .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f devops-sre-api 2>/dev/null || true

                    docker run -d \
                      --name devops-sre-api \
                      -p 8000:8000 \
                      -e APP_NAME="DevOps SRE Assessment API" \
                      -e APP_VERSION="1.0.0" \
                      devops-sre-api
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://host.docker.internal:8000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}