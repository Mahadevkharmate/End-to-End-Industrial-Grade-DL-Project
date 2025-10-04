import os
from box.exceptions import BoxValueError #for handling box errors, that allows dictionary items to be accessed as attributes
from box import ConfigBox #for creating configuration objects that allow attribute-style access to dictionary items
import yaml #for parsing YAML files
import json #for parsing JSON files
import joblib #for saving and loading machine learning models and other objects
from pathlib import Path  #for handling and manipulating filesystem paths
from typing import Any, List, Dict, Union  #for type hinting
from ensure import ensure_annotations  #for runtime type checking of function arguments and return values
from CNNClassifier.logger import logging #custom logging module for logging messages


# Function to read YAML file and return its contents as a dictionary
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """_summary_
    Args:
        path_to_yaml (Path): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        e: _description_

    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path_to_yaml, "r") as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            if content is None:
                raise ValueError(f"The file at {path_to_yaml} is empty.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise e
    

# create_directories function to create directories if they do not exist
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory created at: {path}")


#save_json function to save a dictionary as a JSON file
@ensure_annotations
def save_json(path: Path, data: Dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (Dict): Dictionary to save.(data to be saved in JSON format)
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"JSON file saved at: {path}")

#load_json function to load a JSON file and return its contents as a dictionary
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): Path to the JSON file.
    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object. (ConfigBox allows attribute-style access to dictionary items)
    """
    with open(path, "r") as f:
        content = json.load(f)
    logging.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

#save_bin function to save a binary object using joblib
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves a binary object using joblib.

    Args:
        data (Any): Object to save.(data to be saved in binary format)
        path (Path): Path to the file where the object will be saved.
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"Binary file saved at: {path}")

#load_bin function to load a binary object using joblib
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary object using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded object.(returns the object loaded from the binary file)
    """
    data = joblib.load(filename=path)
    logging.info(f"Binary file loaded from: {path}")
    return data

#get_size function to get the size of a file in KB or MB
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
