import pandas as pd
import numpy as np
from pathlib import Path
import joblib

class Prediction:
    def __init__(self):

        self.model = joblib.load(Path('artifacts\model_training\model.joblib'))

    def predict(self, data):
        return self.model.predict(data)