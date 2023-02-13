# -*- coding: utf-8 -*-
import subprocess
import os
import pytest


#failing healthy disk
def test_failing_healthy_disk():
	HEALTHY_DISK_ID='nzhw -type Disk -local | awk -F " " \'{print$2}\' | awk \'NR>2{print$1}\' | tail -n 1'
	os.system(HEALTHY_DISK_ID)
	hid = subprocess.check_output(HEALTHY_DISK_ID, shell=True,encoding='utf-8',universal_newlines=False).strip()

	os.system('echo y | nzhw failover -id {i} -local'.format(i=hid))
	
	#Functionality will be later shifted to utility module		
	OP='nzhw -type Disk -local | awk -F " " \'{print$4}\' | awk \'NR>2{print$1}\' | tail -n 1'
	res= subprocess.check_output(OP,shell=True,encoding='utf-8',universal_newlines=False).strip()
	assert "Active" == res
