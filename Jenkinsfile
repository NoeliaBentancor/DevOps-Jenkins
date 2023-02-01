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
                script{
                    env.PRUEBA="hola2"
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
