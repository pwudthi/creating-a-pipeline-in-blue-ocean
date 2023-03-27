pipeline {
    agent any
    stages {
        stage('State 1') {
            steps {
                sh "echo 'Running state 1...'"
                // perform State 1 actions here
            }
        }
        stage('State 2') {
            when {
                allOf {
                    previousBuilds()
                    expression { return currentBuild.result == 'SUCCESS' }
                }
            }
            steps {
                sh "echo 'Running state 2...'"
                // perform State 2 actions here
            }
        }
        stage('State 3') {
            when {
                allOf {
                    previousBuilds()
                    expression { return currentBuild.result == 'SUCCESS' }
                }
            }
            steps {
                sh "echo 'Running state 3...'"
                // perform State 3 actions here
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}