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
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m unittest -v'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p runtime
                    cp app.py runtime/app.py

                    cat > runtime/ecosystem.config.js <<EOF
module.exports = {
    apps: [{
        name: "flask-backend",
        script: "app.py",
        interpreter: "${WORKSPACE}/.venv/bin/python",
        cwd: "${WORKSPACE}/runtime"
    }]
};
EOF

                    pm2 startOrReload runtime/ecosystem.config.js --update-env
                    sleep 2
                    curl --fail http://127.0.0.1:5000/health
                '''
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
