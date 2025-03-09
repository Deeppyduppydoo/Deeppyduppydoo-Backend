import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

class TensorflowModel():
    def __init__(self, path_to_model: str):
        self.path_to_model = path_to_model
        self.model = None
    
    def loadModelTensorflow(self):
        model = tf.keras.models.load_model(self.path_to_model)
        self.model = model

    def predictTensorflow(self, img):
        try:
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0
            prediction = self.model.predict(img_array)
            predicted_class_index = np.argmax(prediction, axis=1)
            class_labels = ['Oak', 'Pat', 'Pookkie', 'Praewa', 'Tup']
            predicted_class_label = class_labels[predicted_class_index[0]]
        except Exception as e:
            print(f"Error processing image {img}: {e}")
            predicted_class_label = "Error"

        return predicted_class_label