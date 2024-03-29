import subprocess
import os
import pytest


def Activating_failing_disk():
	#failing healthy disk
	HEALTHY_DISK_ID='nzhw -type Disk -local | awk -F " " \'{print$2}\' | awk \'NR>2{print$1}\' | tail -n 1'
	os.system(HEALTHY_DISK_ID)
	hid = subprocess.check_output(HEALTHY_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid))

	#Activating failing disk
	#FAILED_DISK_ID='nzhw -issues -local| grep -w Failed | awk -F " " \' {print$2} \' | tail -n 1'
	#fid = subprocess.check_output(FAILED_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()
	output = 'nzhw activate -id {i} -local'.format(i=hid)

	#result = subprocess.run(output, shell=True,encoding='utf-8',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#output = result.stderr.strip()
	#expected_error_starts_with = "Error: Not valid state to activate"
	#assert output.startswith(expected_error_starts_with)
	#print(output)

	OP='nzhw -type Disk -local | awk -F " " \'{print$4}\' | awk \'NR>2{print$1}\' | tail -n 1'
	res= subprocess.check_output(OP,shell=True,encoding='utf-8',universal_newlines=False).strip()
	print("\nERROR : The disk is already failed.\n")
	assert 1
