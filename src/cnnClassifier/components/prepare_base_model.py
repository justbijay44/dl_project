import os
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        # loading a pretraining vgg16
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top = self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model = self.model)

    @staticmethod
    # freeze_all - all layers frozen, only new layers (Flatten + Dense) trainable
    # freeze_till = N → freeze all layers except the last N layers.
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer  in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units = 1,
            activation = 'sigmoid',
        )(flatten)

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss = 'binary_crossentropy',
            metrics = ["accuracy"],
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model = self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        model.save(path)