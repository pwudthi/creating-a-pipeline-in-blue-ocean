Map modules = [:]

node {
  script {
    modules.example = load "scripts/example.groovy"
    modules.configs = load "scripts/configs.groovy"
  }
}

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
              choice(choices: modules.example.getProjects(), name: 'Application'),
              string(defaultValue: 'develop', description: '', name: 'branch_name', trim: true),
              booleanParam(defaultValue: true, name: 'check_quality_gate'),
              booleanParam(defaultValue: false, name: 'skip_build')
            ])
          ])
        }
      }
    }

    stage('Build') {
      steps {
        echo "Build"
        script {
          modules.example.otherExampleMethod()
        }
      }
    }

    stage('Test') {
      environment {
        CI = 'true'
      }
      steps {
        echo "Test"
        modules.configs.getTarget()
      }
    }

    stage('Deliver') {
      steps {
        echo "Deliver"
      }
    }

  }
}