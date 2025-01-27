pipeline{
    agent{
        label "test-agent"
    }
    environment{
        IMAGE_NAME = "ghcr.io/sdpxultimate/jenkins-assignment"
        REGISTRY_CREDENTIALS_NAME = "ghcr-credentials"
        REGISTRY_URL = "https://ghcr.io"
        APP_NAME = "web-api"
        ROBOT_REPO = "https://github.com/SDPxUltimate/jenkins-robot"
    }
    stages{
        stage("Install & Run Unittest"){
            steps{
                sh "pip install -r requirements.txt"
                sh "python3 unit_test.py"
            }
        }
        stage("Create Image"){
            steps{
                sh "docker build -t ${IMAGE_NAME}:${BUILD_ID} ."
            }
        }
        // stage("Run Container & Run Robot Testing"){
        //     steps{
        //         sh "docker run -dp 5000:5000 ${IMAGE_NAME}:${BUILD_ID}"
        //         git url: "${ROBOT_REPO}", branch: "${ROBOT_BRANCH}"
        //     }
        // }

    }
}