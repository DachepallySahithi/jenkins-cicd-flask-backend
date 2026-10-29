pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    py -3 -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '.venv\\Scripts\\python.exe -m unittest -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Flask tests passed. Application is ready for deployment.'
            }
        }
    }

    post {
        success {
            echo 'Flask pipeline completed successfully!'
        }
        failure {
            echo 'Flask pipeline failed. Check the console output.'
        }
    }
}