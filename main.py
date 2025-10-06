from src.CNNClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.CNNClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelTrainingPipeline
from src.CNNClassifier.pipeline.training_pipeline import TrainingPipeline
from src.CNNClassifier.logger import logging

STAGE_NAME =" Data Ingestion stage"

try:
    logging.info(f" stage{STAGE_NAME} started..............")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"stage{STAGE_NAME} completed..........")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "PREPARE BASE MODEL"
try:
    logging.info(f" stage{STAGE_NAME} started..............")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f"stage{STAGE_NAME} completed..........")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logging.info(f" stage{STAGE_NAME} started..............")
    training_pipeline = TrainingPipeline()
    training_pipeline.main()
    logging.info(f"stage{STAGE_NAME} completed..........")

except Exception as e:
    logging.exception(e)
    raise e