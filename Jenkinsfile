pipeline 
{
    agent {docker {image 'python:3.7.3'}}
    environment{
        HOLA="hola"
    }
    stages 
    
    {
        stage('Build') 
        {
            steps 
            {
                echo 'Building...'
            }
        }
        stage('Test') 
        {
            steps 
            {
                sh 'python/scripts/blackout-test.py'
                echo 'Testing...'
            }
        }
        stage('Send response to other stages'){
            steps{
                
                script{
                    currentBuild.result = 'SUCCESS'
                }
            }
        }
        stage('Deploy') 
        {
            steps 
            {
                echo 'Deploying...'
            }
        }
    }
}