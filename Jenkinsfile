
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\J\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
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
                bat 'docker build -t jenkins-cicd-app:1.0 .'
            }
        }
    }
}
