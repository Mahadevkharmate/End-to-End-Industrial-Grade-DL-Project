from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import Callbacks
from CNNClassifier.logger import logging
from CNNClassifier.components import Training



#preparing pipeline
class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            callbacks_config = config.get_callbacks_config()    
            callbacks = Callbacks(config = callbacks_config)
            callbacks_list = callbacks.get_tb_chkp_callbacks()

            training_config = config.get_training_config()
            training = Training(config = training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list= callbacks_list)

        except Exception as e:
            raise e