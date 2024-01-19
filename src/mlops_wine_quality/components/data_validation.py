import os
import pandas as pd
from mlops_wine_quality import logger
from mlops_wine_quality.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.local_file_path)
            logger.info(f"Data read from {self.config.local_file_path}")

            # print(data.info())

            data_clos = list(data.columns)
            schema_cols = self.config.all_schema.keys()
            
            for col in data_clos:
                if col not in schema_cols:
                    
                    validation_status = False
                
                else:
                    validation_status = True

                logger.info(f"validation completed with status: {validation_status}")
                
            return validation_status
            
        except Exception as e:

            raise e
