from mlops_wine_quality.components.data_ingestion import DataIngestion
from mlops_wine_quality.configs.configurations import ConfigManger
from mlops_wine_quality import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionStage:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManger()
        dataIngestion_config = config.get_data_ingestion_config()
        dataIngestion = DataIngestion(config=dataIngestion_config)
        dataIngestion.download_data()
        dataIngestion.unzip_data()

if __name__ == "__main__":
    try:
        logger.info(f">>Starting {STAGE_NAME}<</n")
        dataIngestionStage = DataIngestionStage()
        dataIngestionStage.main()
        logger.info(f">>Done {STAGE_NAME}<</n")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e