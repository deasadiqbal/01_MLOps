from mlops_wine_quality.components.data_transformation import DataTransformation
from mlops_wine_quality.configs.configurations import ConfigManger
from mlops_wine_quality import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationStage:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManger()
        dataTransformation_config = config.get_data_transformation_config()
        dataTransformation = DataTransformation(config=dataTransformation_config)
        dataTransformation.train_test_splits()

if __name__ == "__main__":
    try:
        logger.info(f">>Starting {STAGE_NAME}<</n")
        dataTransformationStage = DataTransformationStage()
        dataTransformationStage.main()
        logger.info(f">>Done {STAGE_NAME}<</n")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e