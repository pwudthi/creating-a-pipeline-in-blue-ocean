List<String> pipelineSetup(buildBranch) {
    def buildEnvConfig = [
        1: [
            "branch": "dev_1",
            "buildJob": "Custom-Pipelines/Upper-Folder/dev_1/Deploy"
        ],
        2: [
            "branch": "dev_2",
            "buildJob": "Custom-Pipelines/Upper-Folder/dev_2/Deploy"
        ],
        3: [
            "branch": "dev_3",
            "buildJob": "Custom-Pipelines/Upper-Folder/dev_3/Deploy"
        ]
    ]
    return buildEnvConfig.find { it.value.branch == buildBranch }.value
}

properties([
    parameters([
        choice( choices: ['dev_1', 'dev_2', 'dev_3'], description: 'Branch', name: 'branch')
    ])
])

def piplineConfig = this.&pipelineSetup(branch)
currentBuild.description = "Branch: $branch"

pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo "Hello World: ${branch}"
                build (
                    job: piplineConfig.buildJob,
                    parameters: [string(name: 'title', value: "${piplineConfig.branch}")]
                )
            }
        }
    }
    post {
      always {
        cleanWs()
      }
    }
}
