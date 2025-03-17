pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/wrwksdmoser/flask.git', credentialsId: '10cb4996-9f88-4019-85f7-d3ff7fa8a99b'
            }
        }
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
