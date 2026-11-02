
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\J\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER = 'C:\\Users\\J\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t jenkins-cicd-app:1.0 .'
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    bat(
                        returnStatus: true,
                        script: '"%DOCKER%" rm -f jenkins-cicd-container'
                    )

                    bat '"%DOCKER%" run -d --name jenkins-cicd-container -p 5000:5000 jenkins-cicd-app:1.0'
                }
            }
        }
    }
}
