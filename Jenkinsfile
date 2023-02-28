pipeline 
{
    agent any
    environment{
        FORMAT_TIMESTAMP = "%Y-%m-%dT%H:%M:%S.%fZ"
        MODULES_IGNORED_LOGGING="requests,urllib3"
        REQUEST_MODULE = "requests"
        URL_LIB_MODULE = "urllib3"
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
