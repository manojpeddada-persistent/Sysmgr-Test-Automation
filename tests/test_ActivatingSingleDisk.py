import subprocess
import os
import pytest


def Activating_single_disk():

	#failing healthy disk1
	HEALTHY_DISK_ID1='nzhw -type Disk -local | awk -F " " \'{print$2}\' | awk \'NR>2{print$1}\' | tail -n 1'
	os.system(HEALTHY_DISK_ID1)

	hid1 = subprocess.check_output(HEALTHY_DISK_ID1, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid1))

	#completing failover
	time.sleep(15)

	#failing healthy disk2
	HEALTHY_DISK_ID2='nzhw -type Disk -local | awk -F " " \'{print$2}\' | awk \'NR>2{print$1}\' | head -n 1'
	os.system(HEALTHY_DISK_ID2)

	hid2 = subprocess.check_output(HEALTHY_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid2))

	time.sleep(15)


	#Activating single failed disk
	FAILED_DISK_ID='nzhw -issues -local| grep -w Failed | awk -F " " \' {print$2} \' | tail -n 1'
	fid = subprocess.check_output(FAILED_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	output = 'nzhw activate -id {i} -local'.format(i=fid)

	#result = subprocess.run(output, shell=True,encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	#output = result.stderr.strip()
	#expected_error_starts_with = "Error: cannot activate disk"
	#assert output.startswith(expected_error_starts_with)
	#print(output)
	res= subprocess.check_output(output,shell=True,encoding='utf-8',universal_newlines=False).strip()
	assert "Active" == res
