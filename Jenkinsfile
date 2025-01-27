pipeline{
    agent{
        label "test-agent"
    }
    stages{
        stage("A"){
            agent any
            steps{
                sh "pwd"
                echo "========executing A========"
            }
        }
        stage("B"){
            agent{
                label "pre-prod-agent"
            }
            steps{
                sh "pwd"
                echo "========executing B========"
            }
        }
        stage("C"){
            steps{
                sh "pwd"
                echo "========executing C========"
            }
        }
    }
}