import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

project_name = "CNNClassifier"

# Define the directory structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/__init__.py",
    "research/trials.py",
]

# Create the directories and files
for filepath in list_of_files:
    filepath =Path(filepath) # Convert to Path object for better path handling
    filedir, filename = os.path.split(filepath) # Split into directory and file name seperatly
    
    #if dir is not empty then create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory: {filedir}")

    # checking if file is exist or not if not then creating file 
    # also checking if file has code/data if file is empty then only create otherwise not
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating an empty file:{filepath}")
    else:
        logging.info(f"file is already exists and it is not empty :{filepath}")



    