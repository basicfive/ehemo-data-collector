from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import update

from app.models.scraped_salon import DesignerScrapedSalon, ImageScrapedSalon
from app.models.salon import Salon
from app.schemas.salon_dto import SalonDataDto, ScrapedSalonResponse, SalonsToUpdate


def create_url_from_naver_place_id(naver_place_id):
    return f"https://pcmap.place.naver.com/hairshop/{naver_place_id}/home"

def get_salon_urls_from_salon(salons) -> ScrapedSalonResponse:
    salon_data: List[SalonDataDto] = [
        SalonDataDto(salon_id=salon.id, url=create_url_from_naver_place_id(salon.naver_place_id))
        for salon in salons
    ]
    return ScrapedSalonResponse(
        salon=salon_data,
        total_count=len(salon_data)
    )

class ScrapedSalonService:
    def __init__(self, db: Session):
        self.db = db

    def get_designer_scraped_salon_urls(self, scraped_count: int = 0) -> ScrapedSalonResponse:
        salons: List[Salon] = self.db.query(DesignerScrapedSalon.salon).filter(DesignerScrapedSalon.scrap_count == scraped_count).all() # type: ignore
        return get_salon_urls_from_salon(salons)

    def get_image_scraped_salon_urls(self, scraped_count: int = 0) -> ScrapedSalonResponse:
        salons: List[Salon] = self.db.query(ImageScrapedSalon.salon).filter(ImageScrapedSalon.scrap_count == scarped_count).all() # type: ignore
        return get_salon_urls_from_salon(salons)

    def update_designer_scraped_salons(self, salons_to_update: SalonsToUpdate):
        self.db.execute(
            update(DesignerScrapedSalon.__table__)
            .where(DesignerScrapedSalon.id.in_(salons_to_update.salon_ids)) # type: ignore
            .values(scrap_count=DesignerScrapedSalon.scrap_count + 1)
        )
        self.db.commit()
        return len(salons_to_update.salon_ids)

    def update_image_scraped_salons(self, salons_to_update: SalonsToUpdate):
        self.db.execute(
            update(ImageScrapedSalon.__table__)
            .where(ImageScrapedSalon.id.in_(salons_to_update.salon_ids)) # type: ignore
            .values(scrap_count=ImageScrapedSalon.scrap_count + 1)
        )
        self.db.commit()
        return len(salons_to_update.salon_ids)