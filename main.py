from src.CNNClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
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
