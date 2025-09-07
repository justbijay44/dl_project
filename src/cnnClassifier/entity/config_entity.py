from collections import namedtuple # gives the flexibility of combining tuple + dict + lightweight
import os

DataIngestionConfig = namedtuple("DataIngestionConfig", 
    [
        "root_dir",
        "source_url",
        "local_data_files",
        "unzip_dir",
    ])