from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestionConfig, when we getting the data, below mention return
    type should be (mean we have created custom return type )
    """
    root_dir: Path
    source_url: str
    local_source_file: Path
    unzip_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATS_FILE: Path
    local_file_path: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Data transformation configuration
    """
    root_dir: Path
    data_dir: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_dir: Path
    test_data_dir: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_col: str