import subprocess
import os
import time
import pytest

#failing failed  disk
def test_failing_failed_disk():
	HEALTHY_DISK_ID='nzhw -type Disk -local | awk -F " " \' {print$2} \' | awk \'NR>2{print$1}\''
	hid = subprocess.check_output(HEALTHY_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid))
	time.sleep(15)

	#failing failed disk
	FAILED_DISK_ID='nzhw -issues -local| grep -w Failed | awk -F " " \' {print$2} \' '
	fid = subprocess.check_output(FAILED_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=fid))
	
	OP='nzhw -type Disk -local | awk -F " " \'{print$4}\' | awk \'NR>2{print$1}\' | tail -n 1'
	res= subprocess.check_output(OP,shell=True,encoding='utf-8',universal_newlines=False).strip()
	print("\nERROR : The disk is already failed.\n")
	assert 1

