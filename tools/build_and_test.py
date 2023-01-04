#!/usr/bin/env python3

"""Script to build package and run all tests against builded package."""

#Imports
import os
import sys
import subprocess

#Adding path to sys to use local function defined in src folder
sys.path.append("src")
from py_common.script import run
from py_common.log import log

#Main function def
def main():
    """Run the script."""
    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run run build command
    subprocess.check_call("build/build.py") 

    #Run tox command
    run.run_subprocess_check_call("Tox", "venv checker",["Tox"])    
    
#Main function call
if __name__ == "__main__":
    
    logger = log.get_logger()
    
    try:
        logger.info('Build and test started')
        main()
    except subprocess.CalledProcessError as e:
        logger.exception(f"Build and test failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Build and test failed:  {e}")
        sys.exit(100)  
    else:
        logger.info('Build and test finished - SUCCESS')
    