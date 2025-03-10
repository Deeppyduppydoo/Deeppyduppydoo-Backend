from app.models.model import TensorflowModel, Pytorch_MBv3,Pytorch_ResNet

Vgg16 = TensorflowModel('save_models/model_Augment_2.h5')

Vgg16.loadModelTensorflow()

Mbv3 = Pytorch_MBv3()
Mbv3.loadModel('save_models/mbv3-large-pretrained-imagenet1k-finetuned-handwriting.pth')

Resnet18 = Pytorch_ResNet()
Resnet18.loadModel('saves/models/handwriting_resnet.pth')