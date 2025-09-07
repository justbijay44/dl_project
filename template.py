import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath) # the '/' is for the linux so to avoid path errors pathlib is useful 
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory : {filedir} for {filename} file")

    if (not os.path.exists(filepath)) or  (os.path.getsize(filepath) == 0): 
        #means if filepath doesn't exist or if there is no data inside the file 
        with open(filepath, 'w') as f:
            pass #create file and do nothing
            logging.info(f"Created empty file : {filepath}")
    
    else:
        logging.info(f"A file with name {filename} already exists")
