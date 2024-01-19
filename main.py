from mlops_wine_quality.pipeline.data_ingestion_stage import DataIngestionStage
from mlops_wine_quality.pipeline.data_validation_stage import DataValidationStage
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