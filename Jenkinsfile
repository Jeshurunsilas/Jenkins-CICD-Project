
pipeline {
    agent any

    environment {
        DOCKER = 'C:\\Users\\J\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting calculator project from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t simplybyte-calculator:1.0 .'
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    bat(
                        returnStatus: true,
                        script: '"%DOCKER%" rm -f jenkins-cicd-container'
                    )

                    bat(
                        returnStatus: true,
                        script: '"%DOCKER%" rm -f simplybyte-container'
                    )

                    bat '"%DOCKER%" run -d --name simplybyte-container -p 5000:5000 simplybyte-calculator:1.0'
                }
            }
        }
    }
}
