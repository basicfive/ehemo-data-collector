from pydantic import BaseModel

class NaverMapSearchedUrlCreate(BaseModel):
    url: str
    search_keyword: str

class NaverMapSearchedUrlInDB(BaseModel):
    id: int

    class Config:
        from_attributes=True