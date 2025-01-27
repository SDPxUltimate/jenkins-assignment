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
                echo "========executing B========"
            }
        }
        stage("C"){
            steps{
                echo "========executing C========"
            }
        }
    }
}