from mlops_wine_quality.constants import *
from mlops_wine_quality.utils.common import read_yaml, create_dirs, get_size
from mlops_wine_quality.entity.config_entity import DataIngestionConfig



class ConfigManger:
    def __init__(self,
            config_filepath = CONFIG_FILE_PATH):
        
        self.config = read_yaml(config_filepath)

        create_dirs([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dirs([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_source_file= config.local_source_file,
            unzip_file= config.unzip_dir
        )
        return data_ingestion_config