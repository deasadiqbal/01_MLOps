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