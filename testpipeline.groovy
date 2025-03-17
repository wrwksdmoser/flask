pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                withPythonEnv('python3') {
                    sh 'python --version'
                }
            }
        }
    }
}
