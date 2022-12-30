#!/usr/bin/env python3

'''Script to cleanup run artifacts from repository'''

#Imports
import os
import sys
import subprocess

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.file import dir


#Main function def
def main():
    ''''Main function to run script'''
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run build command
    print('Cleanup run')

    #Run cleanup commands
    print('Cleanup - Build artifacts')
    dir.clean_up_folder_starting_with("build","lib")
    dir.clean_up_folder_starting_with("build","bdist")

    
#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Cleanup failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Cleanup failed:  {e}")
        sys.exit(100)  
    else:
        print('Cleanup finished - SUCCESS')    