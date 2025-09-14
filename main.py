from cnnClassifier.pipeline.stage_01_ingestion import TrainPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PreparePipeLine
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeLine
from cnnClassifier.pipeline.stage_04_evaluate import EvaluationPipeline

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

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    prepare_base_model = PreparePipeLine()
    prepare_base_model.main()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    train_model = ModelTrainingPipeLine()
    train_model.main()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f"{STAGE_NAME} started")
    evaluate_model = EvaluationPipeline()
    evaluate_model.main()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e
