from fastapi import APIRouter, File, UploadFile
from tensorflow.keras.preprocessing import image
from io import BytesIO
from app.utils.load_models import Vgg16
from app.utils.load_models import Mbv3
from app.utils.load_models import Resnet18
from PIL import Image

router = APIRouter()

@router.post('/predict-Vgg16')
async def predict_Vgg16(file: UploadFile):
    img_height,img_width = 224, 224

    contents = await file.read()
    img = image.load_img(BytesIO(contents), target_size=(img_height, img_width))

    prediction, percent = Vgg16.predictTensorflow(img)

    for key in percent:
        percent[key] = float(percent[key])

    return {"filename" : file.filename,"prediction": prediction, "percent": percent}

@router.post('/predict-Mbv3')
async def predict_Mbv3(file: UploadFile):
    contents = await file.read()
    img = Image.open(BytesIO(contents)) # img: path
    prediction , percent = Mbv3.predict(img)

    for key in percent:
        percent[key] = float(percent[key])

    return {"filename" : file.filename,"prediction": prediction, "percent": percent}

@router.post('/predict-Resnet')
async def predict_Resnet(file: UploadFile):
    img_height,img_width = 224, 224

    contents = await file.read()
    img = image.load_img(BytesIO(contents), target_size=(img_height, img_width))

    prediction , percent = Resnet18.predict(img)

    for key in percent:
        percent[key] = float(percent[key])

    return {"filename" : file.filename,"prediction": prediction, "percent": percent}