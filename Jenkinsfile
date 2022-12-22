def modules = [:]
def test_val1 = ''
def test_val2 = ''

pipeline {
  agent any
  options {
    retry(1)
    timeout(time: 3, unit: 'HOURS')
  }
  parameters {
    load("scripts/configs.groovy")
    load("scripts/example.groovy")
    choice(choices: modules.example.getProjects(), name: 'Application'),
    string(defaultValue: 'develop', description: '', name: 'branch_name', trim: true),
    booleanParam(defaultValue: true, name: 'check_quality_gate'),
    booleanParam(defaultValue: false, name: 'skip_build')
  }

  stages {
    stage('Set Parameters') {
      steps {
        echo "Set parameters"
        script {
          test_val1 = 'Test'
        }
      }
    }

    stage('Build') {
      steps {
        echo "Build"
        script {
          otherExampleMethod()
        }
      }
    }

    stage('Test') {
      environment {
        CI = 'true'
      }
      steps {
        echo "Test"
        echo "${test_val1}"
        script {
          getTargetFn()
        }
      }
    }

    stage('Deliver') {
      steps {
        echo "Deliver"
      }
    }

  }
}