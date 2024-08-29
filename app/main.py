from sys import prefix

from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.base import engine
from app.api.v1.api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(router, prefix=settings.API_V1_STR)

@app.get("/health")
def health_check():
    return {"status" : "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
