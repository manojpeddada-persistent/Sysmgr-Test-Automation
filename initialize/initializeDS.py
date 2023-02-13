from class_NPSInfo import NPSInfo
from class_TestInfo import TestInfo
from bs4 import BeautifulSoup
from enum import Enum



class CONFIG(Enum):
	CONFIG_FROM_FILE = 1
	CONFIG_FROM_CMD = 2

class NPSInfoFromCommandLine(NPSInfo):
	def parseDeviceMapConfig():
		abc =10

class NPSInfoFromConfigFile(NPSInfo):
	def __init__(self):
		NPSInfo.__init__(self)
	def parseDeviceMapConfig(self):
		print("In parsing")
		with open('deviceMap.xml', 'r') as f:
			data = f.read()
		Bs_data = BeautifulSoup(data, "xml")
		spus = Bs_data.find('spus')
		self.numberOfSPU = spus.get('num')	
		datapartition = Bs_data.find('datapartitions')
		self.numberOfDataPartition = datapartition.get('num')
		systempartitions = Bs_data.find('systempartitions')
		self.numberOfSystemPartition = systempartitions.get('num')
		disks  = Bs_data.find('disks')
		self.numberOfDisk = disks.get('num')
		hwIdsPerSPU = {}
		
		
	def parseDiskSerialPerSPU(self):
		noOfSpu = 0
		diskserial = {}
		with open('deviceMap.xml', 'r') as f:
			data = f.read()
		Bs_data = BeautifulSoup(data, "xml")
		for x in Bs_data.find_all('spu'):
			noOfSpu = noOfSpu +1
			diskserialNo  = set()
			spuInfo = x.find('systempartitions')
			for y in spuInfo.find_all('logical-partition'):
				disk_serial_num = y.get('lun-guid')
				diskserialNo.add(disk_serial_num)
				diskserial[noOfSpu] = diskserialNo
		return diskserial
	    
	def parseDiskInfo(self):
		disk = {}
		with open('deviceMap.xml', 'r') as f:
			data = f.read()
		Bs_data = BeautifulSoup(data, "xml")
		for x in Bs_data.find_all('disks'):
			for y in x.find_all('disk'):
				disk_serial = y.get('serial-number')
				hw_id = y.get('hwid')
				disk[disk_serial] = hw_id			
		return disk
		
	def getHwidPerSPU(self,DiskSerialPerSPU,diskInfo):
		hwidperSPu = {}
		#print (DiskSerialPerSPU[1])
		for x in range (len(DiskSerialPerSPU)):
		    hwids  = set()	   
		    for value in DiskSerialPerSPU[int(x+1)]:
		    	hwids.add(diskInfo[value])
		    hwidperSPu[x+1] = hwids 
		return hwidperSPu
		
	    
		

class NPSInfoFactory(object):
	def getNPSInfoConfigType(self,type):
		if(type == CONFIG.CONFIG_FROM_FILE):
			return NPSInfoFromConfigFile()
		else:
			return NPSInfoFromCommandLine()
			

def initializeNPSDS():
	print ("Initializing NPSINFO")	
	npsfactoryObj = NPSInfoFactory()
	npsInfo = npsfactoryObj.getNPSInfoConfigType(CONFIG.CONFIG_FROM_FILE)
	npsInfo.parseDeviceMapConfig()
	DiskSerialPerSPU = npsInfo.parseDiskSerialPerSPU()	
	diskInfo = npsInfo.parseDiskInfo()	
	npsInfo.hwIdsPerSPU = npsInfo.getHwidPerSPU(DiskSerialPerSPU,diskInfo)
	return npsInfo
 
def initializeTestDS(testarea, testcase):
	print ("Initializing initializeTestDS")
	testInfo = TestInfo(testarea,testcase)
	return testInfo


	
	
	


	
