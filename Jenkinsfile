peline {
    agent { 
            label "$MachineType" 
        }
    stages {
        stage('Build') {
            steps {
                        sh "python3 main_test.py $TestArea $TestCase $MachineType"
                script {
                         if (manager.logContains('.*Exception*')) {
                                                                    error("Build failed because of this and that..")    
                         }
                }
            }
        }
    }
       post {
              always {
                junit skipPublishingChecks: true, testResults: '**/xmlreport/*.xml'
                echo "This is the end of pipeline script"
                    }

 

    }
}
