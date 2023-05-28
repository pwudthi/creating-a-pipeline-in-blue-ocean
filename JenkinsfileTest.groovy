import org.jenkinsci.plugins.pipeline.modeldefinition.util.FolderNameUtils
import org.jenkinsci.plugins.pipeline.modeldefinition.validator.ModelValidatorImpl
import org.jenkinsci.plugins.pipeline.modeldefinition.validator.SandboxChecker

class JenkinsfileTest extends Specification {
    def "Test Jenkinsfile"() {
        given:
        def pipelineScript = loadJenkinsfile("Jenkinsfile")

        when:
        def validationResult = validateJenkinsfile(pipelineScript)

        then:
        validationResult.isValid() == true
        validationResult.getErrorCount() == 0
    }

    private String loadJenkinsfile(String jenkinsfilePath) {
        // Load the Jenkinsfile content
        return readFile(jenkinsfilePath)
    }

    private ModelValidatorImpl.ValidationResult validateJenkinsfile(String pipelineScript) {
        // Validate the Jenkinsfile using Jenkins Job DSL Plugin and Pipeline Unit testing framework
        def modelValidator = new ModelValidatorImpl(new SandboxChecker(), new FolderNameUtils())
        modelValidator.validate(pipelineScript)
    }

    private String readFile(String filePath) {
        // Read the file content
        new File(filePath).text
    }
}
