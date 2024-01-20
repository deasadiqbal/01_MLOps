from mlops_wine_quality.pipeline.data_ingestion_stage import DataIngestionStage
from mlops_wine_quality.pipeline.data_validation_stage import DataValidationStage
from mlops_wine_quality.pipeline.data_transformation_stage import DataTransformationStage   
from mlops_wine_quality.pipeline.model_training_stage import ModelTrainingStage
from mlops_wine_quality import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>Starting {STAGE_NAME}<</n")
    dataIngestionStage = DataIngestionStage()
    dataIngestionStage.main()
    logger.info(f">>Done {STAGE_NAME}<</n")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>Starting {STAGE_NAME}<</n")
    dataValidationStage = DataValidationStage()
    dataValidationStage.main()
    logger.info(f">>Done {STAGE_NAME}<</n")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>Starting {STAGE_NAME}<</n")
    dataTransformationStage = DataTransformationStage()
    dataTransformationStage.main()
    logger.info(f">>Done {STAGE_NAME}<</n")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>Starting {STAGE_NAME}<</n")
    ModelTrainingStage().main()
    logger.info(f">>Done {STAGE_NAME}<<")
except Exception as e:
    raise e