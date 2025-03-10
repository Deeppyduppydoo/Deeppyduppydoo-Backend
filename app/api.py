from fastapi import FastAPI
from app.predict.predict_api import router
from app.random.random_api import random_router
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="Deeppyduppydoo-Backend",
        description="Deep",
        version="1.0.0",
    )

    return app

app = create_app()

app.include_router(router=router)

app.include_router(router=random_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Deeppyduppydoo-Backend"}