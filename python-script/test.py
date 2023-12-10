from python_terraform import *
import argparse
import sys


def tfcode(parameters):
     print (type(parameters))
     for i in range(len(parameters)):
        tf = Terraform(working_dir='C:\\Users\\acer\Desktop\Terraform-Project\\tfcode')
        #tf.plan(no_color=IsFlagged, refresh=False, capture_output=True)
        approve = {"skip_plan": True}
        #print(tf.plan())
        print(tf.apply(variables={"instancename" : parameters[i]},**approve))
 

if __name__ == '__main__':
    def list_of_strings(arg):
        return arg.split(',')    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--parameters",type=list_of_strings,required=True)
    args = parser.parse_args()
    
    result= tfcode(args.parameters)
    print (result)
    sys.stdout.flush()
    sys.exit(0)