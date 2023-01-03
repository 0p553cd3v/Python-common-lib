#!/usr/bin/env python3

"""Script to run py dock style checker."""

#Imports
import os
import sys
import subprocess

def main():
    """Run the script."""
    #Print script start notification
    print('Docstring coverage run started')

    #Finding build path based on build.py script location
    file_path = os.path.dirname(__file__)
    project_config_path = os.path.abspath(os.path.join(file_path, os.pardir,os.pardir))

    #Changing directory to project config path
    os.chdir(project_config_path)

    #Run pydocstyle command

    subprocess.check_call(
        [
            "pydocstyle",
            "./src",
            "./tools",
            "./build/build.py",
            "./docs/gen_doc.py",
        ]
    ) 

#Main function call
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Pydocstyle run failed: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Pydocstyle run failed: {e}")
        sys.exit(100)
    else:
        print('Pydocstyle run finished - SUCCESS')   