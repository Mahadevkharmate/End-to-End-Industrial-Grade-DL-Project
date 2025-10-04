import os
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from tqdm import tqdm
from CNNClassifier.entity import DataIngestionConfig
from CNNClassifier.logger import logging
from CNNClassifier.utils import get_size

# data Ingestion 
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    #def function to download data from url/any other sources(code will be chnaged)
    def download_file(self):
        logging.info(f"trying to download files")
        if not os.path.exists(self.config.local_data_file):
            logging.info(f"download started......")
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} file downloaded with followinfo info \n{headers} ")
        else:
            logging.info(f"file already exists of size :{get_size(Path(self.config.local_data_file))}")
            
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
        

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str ):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath)==0:
            logging.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    #def function to unzip and clean data
    def unzip_and_clean(self):
        logging.info(f"unzipping file and removing unawanted files")
        with ZipFile(file = self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)
    

    def create_test_data(self):
        """
        separte 30% of data into test data
        """
        pass