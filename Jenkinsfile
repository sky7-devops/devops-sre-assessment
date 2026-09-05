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
                    docker run --rm \
                      --volumes-from jenkins \
                      -w /var/jenkins_home/workspace/devops-sre-assessment \
                      python:3.14-slim \
                      sh -c "pip install -r app/requirements.txt && python -m pytest"
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
                    docker compose down || true
                    docker compose up -d --build
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 10
                    curl -f http://host.docker.internal/health
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

        always {
            echo 'Pipeline execution completed.'
        }
    }
}