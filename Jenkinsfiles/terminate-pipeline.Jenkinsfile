def skipAllStages = false
pipeline {
    agent any
    stages {
        stage('State 1') {
            steps {
                script {
                    try {
                        // perform State 1 actions here
                        sh 'exit 0'
                    } catch (Exception e) {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            skipAllStages = true
                            error "${e.toString()}"
                        }
                    }
                }
            }
        }
        stage('State 2') {
            when {
                expression { !skipAllStages }
            }
            steps {
                script {
                    try {
                        // perform State 2 actions here
                        sh 'exit 1'
                    } catch (Exception e) {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            skipAllStages = true
                            error "${e.toString()}"
                        }
                    }
                }
            }
            post {
                failure {
                    script {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            skipAllStages = true
                            error 'State 2 failed, skipping following stages...'
                        }
                    }
                }
            }
        }
        stage('State 3') {
            when {
                expression { !skipAllStages }
            }
            steps {
                // perform State 3 actions here
                sh 'exit 0'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
