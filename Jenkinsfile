pipeline{
    agent{
        label 'test-agent'
    }
    environment{
        IMAGE_NAME = 'ghcr.io/sdpxultimate/jenkins-assignment'
        REGISTRY_CREDENTIALS = credentials('ghcr-credentials')
        REGISTRY_URL = 'https://ghcr.io'
        APP_NAME = 'web-api'
        ROBOT_REPO = 'https://github.com/sdpxultimate/jenkins-robot'
        ROBOT_BRANCH = 'main'
    }
    stages{
        stage('Install & Run Unittest'){
            steps{
                sh 'pip install -r requirements.txt'
                sh 'python3 unit_test.py'
            }
        }
        stage('Create Image'){
            steps{
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_ID} .'
            }
        }
        stage('Run Container & Run Robot Testing'){
            steps{
                sh 'docker run -dp 5000:5000 --name ${APP_NAME} ${IMAGE_NAME}:${BUILD_ID}'
                git branch: '$ROBOT_BRANCH', url: '$ROBOT_REPO'
                sh 'robot plus.robot'
            }
            post {
                always {
                    sh 'docker stop ${APP_NAME} || true'
                    sh 'docker rm ${APP_NAME} || true'
                }
            }
        }
        stage('Push Image to Registry'){
            steps{
                sh 'echo $REGISTRY_CREDENTIALS_PSW  | docker login ghcr.io -u $REGISTRY_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
        stage('Pull Image from Registry'){
            agent{
                label 'pre-prod-agent'
            }
            steps{
                sh 'echo $REGISTRY_CREDENTIALS_PSW  | docker login ghcr.io -u $REGISTRY_CREDENTIALS_USR --password-stdin'
                sh 'docker pull ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
        stage('Clean & Run Docker Image'){
            agent{
                label 'pre-prod-agent'
            }
            steps{
                sh 'docker stop ${APP_NAME} || true'
                sh 'docker rm ${APP_NAME} || true'
                sh 'docker run -dp 5001:5000 --name ${APP_NAME} ${IMAGE_NAME}:${BUILD_ID}'
            }
        }
    }
    post{
        always{
            sh 'docker system prune -af'
        }
    }
}