pipeline {
  agent none
  options {
      retry(1)
      timeout(time: 3, unit: 'HOURS')
  }
  environment {
      UPDATE_CACHE = "true"
      DOCKER_CREDENTIALS = credentials('dockerhub')
      DOCKER_USERNAME = "${env.DOCKER_CREDENTIALS_USR}"
      DOCKER_PASSWORD = "${env.DOCKER_CREDENTIALS_PSW}"
      DOCKER_CLI_EXPERIMENTAL = "enabled"
      // PULP_PROD and PULP_STAGE are used to do releases
      PULP_HOST_PROD = "https://api.pulp.konnect-prod.konghq.com"
      PULP_PROD = credentials('PULP')
      PULP_HOST_STAGE = "https://api.pulp.konnect-stage.konghq.com"
      PULP_STAGE = credentials('PULP_STAGE')
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