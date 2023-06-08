pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shantanu-2001/EMP-Portal-Project-DevOps.git']]])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'  // Install project dependencies
            }
        }

        stage('Test') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}


