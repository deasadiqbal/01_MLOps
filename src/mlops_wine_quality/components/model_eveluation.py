import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from mlops_wine_quality.utils.common import save_json
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlops_wine_quality.entity.config_entity import ModelEvaluationConfig 
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evel_metrix(self, y_test, predicitons):
        rmse = np.sqrt(mean_squared_error(y_test, predicitons))
        mae = mean_absolute_error(y_test, predicitons)
        r2 = r2_score(y_test, predicitons)
        return rmse, mae, r2

    def start_with_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_dir)
        model_dir = self.config.model_dir

        lr_model = joblib.load(model_dir)

        x_test = test_data.drop(self.config.target_col, axis=1) 
        y_test = test_data[self.config.target_col]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_registry_uri()).scheme

        with mlflow.start_run():
            perdictions = lr_model.predict(x_test)
            (rmse, mae, r2) = self.evel_metrix(y_test, perdictions)

            scores = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }
            save_json(path=Path(self.config.metrix_filename), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(lr_model, "model", registered_model_name="ElasticnetWineModel")
            else:
                mlflow.sklearn.log_model(lr_model, "model")