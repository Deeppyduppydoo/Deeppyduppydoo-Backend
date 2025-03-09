import os
import random
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse



random_router = APIRouter()

base_path = "Images"

@random_router.get('/get-images-list')
def get_random_images_from_dirs():
    images_response = {}
    random_image_paths = []

    try:
        for dir_name in os.listdir(base_path):
            dir_path = os.path.join(base_path, dir_name)

            if os.path.isdir(dir_path):  
                image_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

                if image_files: 
                    random_image_paths.append(os.path.join(dir_path, random.choice(image_files)))
        
        images_response = {"image lists" : random_image_paths}

    except Exception as e:
        print(f"Error : {e}")
        images_response = {"Error" : "Error"}

    return images_response

@random_router.get('/get-image')
def get_image(image_path : str = Query(..., description="Path to the image")):
    print(image_path)
    try:
        if os.path.exists(image_path) and os.path.isfile(image_path):
            return FileResponse(image_path)
        else:
            raise HTTPException(status_code=404, detail="Image not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")