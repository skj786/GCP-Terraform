import json
import subprocess
import argparse
import sys

def tfcode(parameters):

    address ='google_compute_instance.my_test_vm'
    for i in range(len(parameters)):
        project = f"projects/My-First-Project/zones/us-central1-b/instances/{parameters[i]}"
        cmd = f"terraform import {address} {project}"
        print(cmd)
        if args.apply:
            print(subprocess.run(f"{cmd}", shell=True))

if __name__ == '__main__':
    def list_of_strings(arg):
        return arg.split(',')    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--parameters",type=list_of_strings,required=True)
    parser.add_argument('--apply', default=False, action="store_true")
    args = parser.parse_args()
    
    result= tfcode(args.parameters)
    print (result)
    sys.stdout.flush()
    sys.exit(0)
