TestArea = [ "testarea_Disk", #TestArea Disk
	     "testarea_SPU"   #TestArea SPU
           ]  

TestCases = [ "test_FailingHealthyDisk", #TestCase Failing healthy disk
              "test_FailingFailedDisk", #TestCase Failing failed disk
              "test_ActivatingAlreadyActiveDisk", #TestCase Activating active disk
	      "test_FailingFailingDisk", #TestCase Failing failing disk
	      "test_AcivatingFailedDisk", #TestCase Activating Failed disk
	      "All" # Executing all cases
           ]
