class TestInfo:
    __instance = None
    def getInstance(self):
      """ Static access method. """
      if TestInfo.__instance == None:
          TestInfo()
      return TestInfo.__instance

    def __init__(self,testCaseArea,testCaseName):
        if TestInfo.__instance != None:
           print("This class is a singleton!")
        else:
            self.testCaseArea = testCaseArea
            self.testCaseName = testCaseName
   