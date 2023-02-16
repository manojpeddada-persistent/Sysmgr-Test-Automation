from subprocess import call
import os
from configs.constants import TestArea,TestCases

class TestFramework:
    def __init__(self,testarea,testcase,server):       
           self.testarea = testarea
           self.testcase = testcase
           self.server = server
    def validate_NPSInfo(self,npsInfo):  
    	print ("Validating")   
    def validate_TestInfo(self,testInfo):  
         if testInfo.testCaseArea in TestArea:
            print("TestCaseArea is valid:",testInfo.testCaseArea)
         else:
            print("Error: TestCase Area is invalid:",testInfo.testCaseArea)
            return
     
         if testInfo.testCaseName in TestCases:
            print("TestCase Name is valid:",testInfo.testCaseName)
         else:
            print("Error: TestCase Name is invalid:",testInfo.testCaseName)
            return

    def execute_test(self,testcase,testarea):  
        if testcase == "All":
            os.system('pytest ./tests --junitxml=./xmlreport/output.xml')
        else :
            os.system('pytest ./tests/{tc}.py --junitxml=./xmlreport/output.xml'.format(tc = testcase))
