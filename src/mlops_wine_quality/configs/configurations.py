from mlops_wine_quality.constants import *
from mlops_wine_quality.utils.common import read_yaml, create_dirs, get_size
from mlops_wine_quality.entity.config_entity import (DataIngestionConfig, 
                                                     DataValidationConfig,
                                                     DataTransformationConfig)



class ConfigManger:
    def __init__(self,
            config_filepath = CONFIG_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)

        create_dirs([self.config.artifacts_root])

    # get data ingestion config
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
    
    # get data validation config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_dirs([config.root_dir])
        
        return DataValidationConfig(
            root_dir= config.root_dir,
            STATS_FILE= config.STATS_FILE,
            local_file_path= config.local_file_path,
            all_schema= schema            
        )
    
    # get data transformation config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_dirs([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir,
        )

        return data_transformation_config