pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m pytest
                '''
            }
        }

        stage('Generate Coverage') {
            steps {
                sh '''
                . venv/bin/activate
                python -m pytest --cov=app --cov-report=xml
                '''
            }
        }

    }

}