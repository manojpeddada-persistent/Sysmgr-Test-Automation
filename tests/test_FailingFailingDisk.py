import subprocess
import os
import pytest


#failing healthy disk
def test_failover_failing_disk():

	#old tried script
	'''
	import subprocess
 
	diskid = subprocess.check_output("nzhw -issues -local | awk 'NR==3 {print $2}'", shell=True, encoding='utf-8').strip()
	 
	failcommand = "nzhw failover -id " + diskid
	result = subprocess.run(failcommand, shell=True, input="y", encoding='utf-8')
	'''

	#new script
	HEALTHY_DISK_ID='nzhw -type Disk -local | awk -F " " \' {print$2} \' | awk \'NR>2{print$1}\''
	os.system(HEALTHY_DISK_ID)

	hid = subprocess.check_output(HEALTHY_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid))

	#failing failing disk
	FAILING_DISK_ID='nzhw -issues -local| grep -w Failing | awk -F " " \' {print$2} \' '
	fid = subprocess.check_output(FAILING_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=fid))
	
	OP='nzhw -type Disk -local | awk -F " " \'{print$4}\' | awk \'NR>2{print$1}\' | tail -n 1'
	res= subprocess.check_output(OP,shell=True,encoding='utf-8',universal_newlines=False).strip()

	print("\nERROR : The disk is already failed.\n")
	assert 1


