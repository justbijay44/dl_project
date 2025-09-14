from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import PrepareCallback, Training
from cnnClassifier import logger

class ModelTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callback_config = config.get_prepare_callback_config()
        prepare_callback = PrepareCallback(config=prepare_callback_config)
        callback_list = prepare_callback.get_tb_chpt_callback()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )