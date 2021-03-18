'''
To run the job:

$ pyats run job IOS_XE_magic_carpet_job.py --testbed-file testbed/testbed.yaml

'''

import os

def main(runtime):
    # Find the location of the script in relation to the job file
    testscript = os.path.join(os.path.dirname(__file__), 'IOS_XE_magic_carpet.py')
    
    # run script
    runtime.tasks.run(testscript=testscript)