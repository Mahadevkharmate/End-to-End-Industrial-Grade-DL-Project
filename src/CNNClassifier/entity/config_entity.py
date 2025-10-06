 
from pathlib import Path 
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: List[int]
    params_include_top: bool
    params_classes: int
    params_weights: str
    params_learning_rate: float


@dataclass(frozen=True)
class CallabacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_augmentation: bool
    params_image_size: List[int]