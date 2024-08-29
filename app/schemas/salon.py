from pydantic import BaseModel

class SalonCreate(BaseModel):
    naver_place_id: int
    name: str

class SalonInDB(BaseModel):
    id: int

    class Config:
        from_attributes=True