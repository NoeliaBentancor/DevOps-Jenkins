pipeline 
{
    agent any
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
                sh 'python3 scripts/blackout-test.py'
                echo 'Testing...'
            }
        }
        stage('Send response to other stages'){
            steps{
                
                sh 'python3 scripts/test.py'
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
