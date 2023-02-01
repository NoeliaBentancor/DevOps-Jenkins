pipeline 
{
    agent any
    environment{
        PRUEBA="hola"
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
                //save in a variable result of script blackout test
                PRUEBA2= sh(script: 'python3 scripts/blackout-test.py', returnStdout: true)
                script{
                    env.PRUEBA=PRUEBA2
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
