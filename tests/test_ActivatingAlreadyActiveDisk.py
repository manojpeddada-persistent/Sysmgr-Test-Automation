import os

import subprocess

def test_activatingAlreadyActiveDisk():
    disk_id='nzhw -type Disk -local | awk -F " " \'{print$2}\' | awk \'NR>2{print$1}\' | tail -n 1'
    #os.system(disk_id)
    hid = subprocess.check_output(disk_id, shell=True,encoding='utf-8',universal_newlines=False).strip()

    output = 'nzhw activate -id {i} -local'.format(i=hid)    

    result = subprocess.run(output, shell=True,encoding='utf-8',stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stderr.strip()

    expected_error_starts_with = "Error: cannot activate disk"

    assert output.startswith(expected_error_starts_with)
    print(output)
