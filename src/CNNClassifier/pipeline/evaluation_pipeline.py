from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import Evaluation
from CNNClassifier.logger import logging

class EvaluationTraining:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_validation_data_config()
            evalavation =Evaluation(config = evaluation_config)
            evalavation.evaluation()
            evalavation.save_score()
        except Exception as e:
            raise e