from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Settings(BaseModel):
    API_V1_STR:str = "/api/v1"
    PROJECT_NAME:str = "ehemo-api"
    DATABASE_URL:str = os.getenv("DATABASE_URL")

settings = Settings()