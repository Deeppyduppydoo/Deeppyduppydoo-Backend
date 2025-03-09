import os
import random
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path


random_router = APIRouter()

BASE_IMAGE_PATH = Path("images")

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

@random_router.get('/get-images-list')
def get_random_images_from_dirs():
    images_response = {}
    random_image_paths = []

    try:
        for dir_name in os.listdir(BASE_IMAGE_PATH):
            dir_path = os.path.join(BASE_IMAGE_PATH, dir_name)

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

    sanitized_path = BASE_IMAGE_PATH / Path(image_path).name

    print(Path(image_path).name)

    if not sanitized_path.is_relative_to(BASE_IMAGE_PATH):
            raise HTTPException(status_code=403, detail="Forbidden: Access to this file is not allowed.")

    if sanitized_path.exists() and sanitized_path.is_file():
        file_extension = sanitized_path.suffix.lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=415, detail="Unsupported file type.")
        return FileResponse(sanitized_path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")