import os
import yaml
import json
import joblib
import base64

from typing import Any
from pathlib import Path
from box import ConfigBox
from cnnClassifier import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError

# ensure_annotations gives error if datatype we are working are different
@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
        Loading the YAML file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
            # With Configbox we can access the dict as the obj
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dir(path_to_dir: list, verbose=True):
    # when verbose=True. function will log a message each time it creates a directory
    """
        Creating directory
    """
    for path in path_to_dir:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        
        if verbose:
            logger.info(f"Directory created succesfully at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent= 4) # intent basically makes the json more readable each key-value pair is in new line

    logger.info(f"Json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Json loaded succesfully from path : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(value=data, filename=path)
    logger.info(f'Binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f'Binary file loaded from: {path}')

    return data

@ensure_annotations
def get_size(path=Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImage):
    with open(croppedImage, 'rb') as f:
        return base64.b64encode(f.read())