#prepare my components
# import tensorflow as tf

import os
import tensorflow as tf
from zipfile import ZipFile
import urllib.request as request
import time
from CNNClassifier.entity import CallabacksConfig

class Callbacks:
    def __init__(self, config: CallabacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_runing_log_dir = os.path.join(self.config.tensorboard_root_log_dir,f"tb_logs_at_{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir = tb_runing_log_dir)
    
    @property
    def _create_chkp_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only = True
        )

    #define methods to get tensorboard checkpoints
    def get_tb_chkp_callbacks(self):
        return[
            self._create_tb_callbacks,
            self._create_chkp_callbacks
        ]