pipeline {
    agent any

    environment {
        // Replace with your Docker Hub credentials ID (created in Jenkins)
        DOCKER_HUB_CREDENTIALS_ID = 'a806cdfc-0b3a-40ee-9406-0ebc4c6110dc'
        IMAGE_NAME = 'gajapathi22/hello-world-python'
        IMAGE_TAG = '1'
        GIT_BRANCH = 'master'
        REPO_URL = 'https://github.com/AnuragJaiswal14/CodeforComplianceScanner.git'
        SCRIPT_PATH = '/home/gajapathi/Desktop/Learnings/CodeforComplianceScanner/script.sh'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${env.GIT_BRANCH}", url: "${env.REPO_URL}"
            }
        }

        stage('Execute Bash Script') {
            steps {
                sh "chmod +x ${env.SCRIPT_PATH}"
                sh "sudo bash ${env.SCRIPT_PATH}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${env.IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${env.DOCKER_HUB_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${env.IMAGE_NAME}:${env.IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after each run
        }
    }
}