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
                //save in a variable the RESULT of python script
                //save in a variable the RESULT of python script
                script{
                    def version_numbers = sh(script: 'python3 scripts/test.py', returnStdout: true)

                    env.PRUEBA = version_numbers
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
