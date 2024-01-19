from mlops_wine_quality.entity.config_entity import DataIngestionConfig
from pathlib import Path
from mlops_wine_quality.constants import *
from mlops_wine_quality.utils.common import get_size
import os
import urllib.request as request
import zipfile
from mlops_wine_quality import logger



class DataIngestion:
    def __init__(self,
                  config = DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_source_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_source_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_source_file))}")

    def unzip_data(self):
        unzip_path = self.config.unzip_file
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_source_file, "r") as f:
            f.extractall(unzip_path)