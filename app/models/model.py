import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image

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
    
class Pytorch_MBv3():
    def __init__(self):
        self.model = torchvision.models.mobilenet_v3_large(weights='IMAGENET1K_V1')
        self.model.classifier[3] = nn.Linear(in_features=1280, out_features=5, bias=True)

    def loadModel(self,path_to_model :str):
        self.model.load_state_dict(torch.load(path_to_model,map_location=torch.device('cpu')))
        
    def predict(self, img):
        class_labels = ['Oak', 'Pat', 'Pookkie', 'Praewa', 'Tup']
        try:
            transform = transforms.Compose(
                        [transforms.Resize((224, 224)),
                         transforms.Grayscale(num_output_channels=3),
                         transforms.ToTensor(),
                         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
            img_tensor = transform(img)
            img_tensor = img_tensor.unsqueeze(0)
            self.model.eval()
            with torch.no_grad():
                outputs = self.model(img_tensor)
                # prob = torch.nn.functional.softmax(outputs, dim=1) #to probability เผื่อใช้
                top_class = torch.argmax(outputs)
                predicted_class_label = class_labels[top_class]
        except Exception as e:
            print(f"Error processing image {img}: {e}")
            predicted_class_label = "Error"

        return predicted_class_label
    
class Pytorch_ResNet:
    def __init__(self):
        self.model = torchvision.models.resnet18(weights=None)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 5)

    def loadModel(self, path_to_model: str):
        self.model.load_state_dict(torch.load(path_to_model, map_location=torch.device('cpu')))
        self.model.eval()

    def predict(self, img):
        class_labels = ['Oak', 'Pat', 'Pookkie', 'Praewa', 'Tup']
        try:
            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.Grayscale(num_output_channels=3),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
            
            img_tensor = transform(img).unsqueeze(0)
            
            with torch.no_grad():
                outputs = self.model(img_tensor)
                top_class = torch.argmax(outputs)
                predicted_class_label = class_labels[top_class.item()]
                
        except Exception as e:
            print(f"Error processing image: {e}")
            predicted_class_label = "Error"

        return predicted_class_label
        