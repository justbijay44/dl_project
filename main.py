from cnnClassifier.pipeline.stage_01_ingestion import TrainPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    data_ingestion = TrainPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e


