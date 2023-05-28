pipeline {
    agent any

    stages {

        stage('Install Groovy') {
            steps {
                tool name: 'Groovy-4.0.9', type: 'hudson.plugins.groovy.GroovyInstallation'
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building...'
                    // Your build steps here
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    checkout scm
                    // Your test steps here
                    sh 'groovy JenkinsfileTest.groovy'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying...'
                    // Your deployment steps here
                }
            }
        }
    }
}
