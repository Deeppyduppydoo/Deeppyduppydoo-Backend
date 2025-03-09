from fastapi import FastAPI
from app.predict.predict_api import router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Deeppyduppydoo-Backend",
        description="Deep",
        version="1.0.0",
    )

    return app

app = create_app()

app.include_router(router=router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Deeppyduppydoo-Backend"}