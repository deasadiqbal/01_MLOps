import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlops_wine_quality import logger
from mlops_wine_quality.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,
                 config: DataTransformationConfig):
        self.config = config

    def train_test_splits(self):
        df = pd.read_csv(self.config.data_dir)

        train, test = train_test_split(df)
        # svae the train and test data csv in data transformation folders
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'))

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")

        print(train.shape)
        print(test.shape)