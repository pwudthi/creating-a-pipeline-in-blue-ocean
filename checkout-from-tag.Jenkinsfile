pipeline {
    agent any
    parameters {
        gitParameter name: 'TAG', branch: 'develop', branchFilter: 'tag/(.*)', description: '', type: 'PT_TAG', defaultValue: '0.0.0.1', sortMode: 'DESCENDING_SMART'
    }
    stages {
        stage('Checkout from TAG') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: "${params.TAG}"]],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          gitTool: 'Default',
                          submoduleCfg: [],
                          userRemoteConfigs: [[url: 'https://github.com/pwudthi/creating-a-pipeline-in-blue-ocean.git']]
                        ])
            }
        }
    }
}