from pydantic import BaseModel
from typing import List

class SalonDataDto(BaseModel):
    salon_id: int
    url: str

class ScrapedSalonResponse(BaseModel):
    salon: List[SalonDataDto]
    total_count: int

class SalonsToUpdate(BaseModel):
    salon_ids: List[int]