from app.models.model import TensorflowModel

Vgg16 = TensorflowModel('save_models/model_Augment_2.h5')

Vgg16.loadModelTensorflow()