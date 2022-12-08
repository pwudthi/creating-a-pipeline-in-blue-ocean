pipeline {
  agent any
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
              string(defaultValue: 'develop', description: '', name: 'branch_name', trim: true),
              booleanParam(defaultValue: true, name: 'check_quality_gate'),
              booleanParam(defaultValue: true, name: 'skip_build')
            ])
          ])
        }
      }
    }

    stage('Build') {
      steps {
        echo "Build"
        script {
          def custom_functions = load "scripts/example.groovy"
          custom_functions.otherExampleMethod()
        }
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