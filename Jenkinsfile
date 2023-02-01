pipeline 
{
    agent any
    
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
                //save in a variable result of script blackout test
                script{
                    def version_numbers = bat(script: 'python3 scripts/test.py', returnStdout: true)

                    env.PRUEBA = warName
                }

                
               
                echo 'Testing...'
            }
        }
        stage('Send response to other stages'){
            steps{
                echo "Response: ${env.PRUEBA}"
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
