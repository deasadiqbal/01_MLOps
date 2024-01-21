from mlops_wine_quality.configs.configurations import ConfigManger
from mlops_wine_quality.components.model_eveluation import ModelEvaluation
from mlops_wine_quality import logger


STAGE_NAME = "Model Evaluation"
class ModelEvaluationStage:
    def __init__(self):
        pass 
    def main(self):
        config = ConfigManger()
        model_evaluation_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(model_evaluation_config)
        model_eval.start_with_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>Starting {STAGE_NAME}<</n")
        ModelEvaluationStage().main()
        logger.info(f">>Done {STAGE_NAME}<<")
    except Exception as e:
        raise e 