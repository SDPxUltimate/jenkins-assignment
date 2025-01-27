pipeline{
    agent{
        label "test-agent"
    }
    stages{
        stage("A"){
            agent any
            steps{
                echo "========executing A========"
            }
        }
        stage("B"){
            agent{
                label "pre-prod-agent"
            }
            steps{
                echo "========executing A========"
            }
        }
        stage("C"){
            steps{
                echo "========executing A========"
            }
        }
    }
}