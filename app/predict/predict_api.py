from fastapi import APIRouter, File, UploadFile
from tensorflow.keras.preprocessing import image
from io import BytesIO
from app.utils.load_models import Vgg16

router = APIRouter()

@router.post('/predict-Vgg16')
async def predict_Vgg16(file: UploadFile):
    img_height,img_width = 224, 224

    contents = await file.read()
    img = image.load_img(BytesIO(contents), target_size=(img_height, img_width))

    prediction = Vgg16.predictTensorflow(img)

    return {"filename" : file.filename,"prediction": prediction}