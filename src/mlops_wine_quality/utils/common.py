import os
import yaml
import joblib
import json
from pathlib import Path 
from mlops_wine_quality import logger
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations



@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
    """
    Reads yaml file and returns a ConfigBox object
    """
    try:
        with open(yaml_file_path, "r") as f:
            content = yaml.safe_load(f)
            config = ConfigBox(content)
            logger.info("Yaml file loaded successfully")
            return config
    except BoxValueError:
        raise ("Please provide a valid yaml file")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_dirs(path_to_dirs: list, verbose=True):
    """
    creates directories
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Saved json file at {path}")


@ensure_annotations
def load_json(path: Path):
    """
    Loads json file
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f"Loaded json file from {path}")
    return data


@ensure_annotations
def save_binary(data, path: Path):
    """
    Saves binary file
    """
    joblib.dump(data, path)
    logger.info(f"Saved binary file at {path}")


@ensure_annotations
def load_binary(path: Path):
    """
    Loads binary file
    """
    data = joblib.load(path)
    logger.info(f"Loaded binary file from {path}")
    return data


@ensure_annotations
def get_size(path: Path):
    """
    Returns size of file
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"