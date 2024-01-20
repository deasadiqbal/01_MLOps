# import elasticnet_regression
from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd
from mlops_wine_quality import logger
from mlops_wine_quality.entity.config_entity import ModelTrainingConfig
import os

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    def start_tarining(self):
        train_data = pd.read_csv(self.config.train_data_dir)
        test_data = pd.read_csv(self.config.test_data_dir)

        x_train = train_data.drop(self.config.target_col, axis=1)
        y_train = train_data[self.config.target_col]
        x_test = test_data.drop(self.config.target_col, axis=1) 
        y_test = test_data[self.config.target_col]

        lr_model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        lr_model.fit(x_train, y_train)
        # svae the model
        joblib.dump(lr_model, os.path.join(self.config.root_dir, self.config.model_name))

