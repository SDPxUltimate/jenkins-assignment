pipeline{
    agent{
        label "test-agent"
    }
    stages{
        stage("A"){
            agent any
            steps{
                sh "pwd"
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} at node ${env.NODE_NAME}"
            }
        }
        stage("B"){
            agent{
                label "pre-prod-agent"
            }
            steps{
                sh "pwd"
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} at node ${env.NODE_NAME}"
            }
        }
        stage("C"){
            steps{
                sh "pwd"
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL} at node ${env.NODE_NAME}"
            }
        }
    }
}