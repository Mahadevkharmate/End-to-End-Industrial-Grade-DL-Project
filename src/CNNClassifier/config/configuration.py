from src.CNNClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.CNNClassifier.utils.common import read_yaml, create_directories
from pathlib import Path 
import sys
import os
from CNNClassifier.entity import (DataIngestionConfig,
                                  PrepareBaseModelConfig,
                                  CallabacksConfig,
                                  TrainingConfig
                                  )
class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH
                 ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file =  config.local_data_file,
            unzip_dir = config.unzip_dir
            )
        return data_ingestion_config
    

    #these are required configuration to prepare base model from keras VGG16
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        params =self.params

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path =  Path(config.updated_base_model_path),
            params_image_size = params.IMAGE_SIZE,
            params_include_top = params.INCLUDE_TOP,
            params_classes =  params.CLASSES,
            params_weights = params.WEIGHTS,
            params_learning_rate = params.LEARNING_RATE

        )
        return prepare_base_model_config
    
    #preparing_callbacks_configurations
    def get_callbacks_config(self) -> CallabacksConfig:
        config = self.config.callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)

        create_directories([
            Path(config.tensorboard_root_log_dir),
            Path(model_ckpt_dir)
            ])

        callbacks_config = CallabacksConfig(
            root_dir = Path(config.root_dir),
            tensorboard_root_log_dir = Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath)
            )
        return callbacks_config
    
    #preparing traing configuration
    def get_training_config(self) ->TrainingConfig:
        training = self.config.training #for root_dir, trained_model_path
        prepare_base_model = self.config.prepare_base_model #for updated_base_model_path
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "PetImages") #for training data
        params = self.params  #for params

        create_directories([Path(training.root_dir)]) #to create training- dir
        
        trainig_config = TrainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_augmentation = params.AUGMENTATION,
            params_image_size = params.IMAGE_SIZE
            )
        return trainig_config

