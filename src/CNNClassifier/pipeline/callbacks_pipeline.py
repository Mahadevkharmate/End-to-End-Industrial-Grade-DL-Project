from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import Callbacks
from CNNClassifier.logger import logging

class CallbacksTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            callbacks_config = config.get_callbacks_config()    
            callbacks = Callbacks(config = callbacks_config)
            callbacks_list = callbacks.get_tb_chkp_callbacks()
        except Exception as e:
            raise e
