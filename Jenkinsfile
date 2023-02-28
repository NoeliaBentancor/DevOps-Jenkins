pipeline 
{
    agent any
    environment{
        FORMAT_TIMESTAMP="%Y-%m-%dT%H:%M:%S.%fZ"
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
                script{
                    def version_numbers = sh(script: 'python3 scripts/blackout-test.py', returnStdout: true)
                    env.PRUEBA = version_numbers
                }
             
                
               
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
