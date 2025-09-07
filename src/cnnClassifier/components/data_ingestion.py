import os
from pathlib import Path 
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from cnnClassifier.entity import DataIngestionConfig
from cnnClassifier.utils import get_size
from cnnClassifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Downloading the file..")
        os.makedirs(os.path.dirname(self.config.local_data_files), exist_ok=True)

        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename= self.config.local_data_files
            )
            logger.info(f"{filename} has been downloaded with info:\n{headers}")
        else:
            logger.info(f"File already exists")

    # _sth are hidden methods from the user that developers can only access    
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith('.jpg') and ('Cat' in f or 'Dog' in f)]
    
    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"Removing file : {target_filepath} of size is {get_size(Path(target_filepath))}")
            os.remove(target_filepath)
    
    def unzip_n_clean(self):
        logger.info("Unzipping and cleaning the file..")
        with ZipFile(file = self.config.local_data_files, mode='r') as zf:
            list_of_files = zf.namelist()
            updated_list = self._get_updated_list_of_files(list_of_files)

            for f in tqdm(updated_list):
                self._preprocess(zf, f, self.config.unzip_dir)    