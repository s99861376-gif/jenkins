pipeline{
    agent any
    stages{
        stage('Setup'){
            steps{
                echo 'Installing dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Build and Test'){
            steps{
                echo 'Running ml pipeline...'
                bat 'python ml-pipeline.py'
            }
            }
        }
        post{
            success {
                echo ' Pipeline Success - Model Validated '
        }
            failure {
                echo ' Pipeline Failed - Check logs '
        }
        }
}
