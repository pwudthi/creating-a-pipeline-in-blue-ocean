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