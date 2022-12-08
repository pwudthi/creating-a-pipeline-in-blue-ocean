pipeline {
  agent none
  options {
      retry(1)
      timeout(time: 3, unit: 'HOURS')
  }
  environment {
      UPDATE_CACHE = "true"
      DEBUG = 0
  }
  stages {
    stage('Set Parameters') {
      steps {
        echo "Set parameters"
        script {
          properties([
            parameters([
                choice(
                    choices: ['ONE', 'TWO'],
                    name: 'PARAMETER_01'
                ),
                booleanParam(
                    defaultValue: true,
                    description: '',
                    name: 'BOOLEAN'
                ),
                string(
                    defaultValue: 'scriptcrunch',
                    name: 'STRING-PARAMETER',
                    trim: true
                )
            ])
          ])
        }
      }
    }

    stage('Build') {
      steps {
        echo "Build"
      }
    }

    stage('Test') {
      environment {
        CI = 'true'
      }
      steps {
        echo "Test"
      }
    }

    stage('Deliver') {
      steps {
        echo "Deliver"
      }
    }

  }
}