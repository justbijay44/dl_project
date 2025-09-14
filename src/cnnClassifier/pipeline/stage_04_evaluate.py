from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import Evalaution
from cnnClassifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evalaution = Evalaution(config=val_config)
        evalaution.evaulate()
        evalaution.save_score()
            