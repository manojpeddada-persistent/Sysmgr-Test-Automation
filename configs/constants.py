TestArea = [ "testarea_Disk", #TestArea Disk
	     "testarea_SPU"   #TestArea SPU
           ]  

TestCases = [ "test_FailingHealthyDisk", #TestCase Failing healthy disk
              "test_FailingFailedDisk", #TestCase Failing failed disk
              "test_ActivatingAlreadyActiveDisk", #TestCase Activating active disk
	      "test_FailingFailingDisk", #TestCase Failing failing disk
	      "test_ActivatingFailedDisk", #TestCase Activating Failed disk
	      "test_ActivatingSingleDisk", #TestCase activating Single disk
	      "All" # Executing all cases
           ]
