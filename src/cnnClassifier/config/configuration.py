import os
from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils import read_yaml, create_dir
from cnnClassifier.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, param_filepath = PARAM_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir =  config.root_dir,
            source_url = config.source_url,
            local_data_files = config.local_data_files,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config