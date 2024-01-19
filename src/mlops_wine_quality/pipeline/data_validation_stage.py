from mlops_wine_quality.components.data_validation import DataValidation
from mlops_wine_quality.configs.configurations import ConfigManger
from mlops_wine_quality import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationStage:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManger()
        dataValidation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=dataValidation_config)
        data_validation.validate()

if __name__ == "__main__":
    try:
        logger.info(f">>Starting {STAGE_NAME}<</n")
        dataValidationStage = DataValidationStage()
        dataValidationStage.main()
        logger.info(f">>Done {STAGE_NAME}<</n")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e