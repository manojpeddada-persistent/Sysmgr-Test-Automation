pipeline {
    agent { 
            label "$MachineType" 
        }
    stages {
        stage('Build') {
            steps {
              //checkout([$class: 'GitSCM', 
                //branches: [[name: '*/main']],
                //doGenerateSubmoduleConfigurations: false,
                //extensions: [[$class: 'CleanCheckout']],
                //submoduleCfg: [], 
              
                // userRemoteConfigs: [[url: 'https://github.com/nzuser2023/Sysmgr-Automation.git']]])
                sh "python3 Test.py $TestArea $TestCase $MachineType"
                
          }
        }
    }
   	post {
      		always {
        		junit skipPublishingChecks: true, testResults: '**/xmlreport/*.xml'
 
                       }
    	      }
}
