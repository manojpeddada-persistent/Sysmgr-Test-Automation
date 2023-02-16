import sys
from classes.class_TestFramework import TestFramework
import configs
import initialize.initializeDS as initializeDS

# Parse the input from front end
#testarea = sys.argv[config.TESTAREA]
#testcase = sys.argv[config.TESTCASENAME]
#server = sys.argv[config.SERVER]

testarea = sys.argv[1]
testcase = (sys.argv[2]).rstrip(',')
server = sys.argv[3]

#Initialize the data Structure
npsInfo = initializeDS.initializeNPSDS()
testInfo = initializeDS.initializeTestDS(testarea,testcase)
print (npsInfo.numberOfSPU)
print (npsInfo.numberOfDisk)
print (npsInfo.numberOfDataPartition)
print (npsInfo.numberOfSystemPartition)
for x in range(int(npsInfo.numberOfSPU)):
    print (npsInfo.hwIdsPerSPU[int(x+1)])
#initializeDS.parseDeviceMapConfig()

testFramework = TestFramework(testarea,testcase,server)
#Validate the NPS Info
testFramework.validate_NPSInfo(npsInfo)
#Validate the TestInfo
testFramework.validate_TestInfo(testInfo)
#Execute the actual test
testFramework.execute_test(testcase,testarea)
