pipeline {
    agent any
    parameters {
        load('path/to/script.groovy')
    }
    stages {
        stage('Build') {
            steps {
                // build steps go here
            }
        }
        stage('Test') {
            steps {
                // test steps go here
                echo "Parameter value: ${params.PARAMETER_NAME}"
            }
        }
        stage('Deploy') {
            steps {
                // deploy steps go here
            }
        }
    }
}

