from mlops_wine_quality.components.model_training import ModelTraining
from mlops_wine_quality.configs.configurations import ConfigManger
from mlops_wine_quality import logger

STAGE_NAME = "Model Training Stage"
class ModelTrainingStage:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManger().get_model_training_config()
        logger.info("Training started")
        training = ModelTraining(config)
        training.start_tarining()
        logger.info("Training completed")

if __name__ == "__main__":
    try:
        logger.info(f">>Starting {STAGE_NAME}<</n")
        ModelTrainingStage().main()
        logger.info(f">>Done {STAGE_NAME}<<")
    except Exception as e:
        raise e