from sqlalchemy.orm import Session
from typing import List

from app.models.scraped_salon import ImageScrapedSalon, DesignerScrapedSalon
from app.schemas.salon import SalonCreate
from app.models.salon import Salon

class SalonService:
    def __init__(self, db: Session):
        self.db = db

    def create_salons(self, salons: List[SalonCreate]):
        existing_naver_ids = self.get_existing_naver_ids_from([salon.naver_place_id for salon in salons])
        new_salons = [salon for salon in salons if salon.naver_place_id not in existing_naver_ids]

        # 미용실 추가
        salon_objects = [Salon(**salon.model_dump()) for salon in new_salons]
        self.db.add_all(salon_objects)
        self.db.flush()

        # 디자이너 / 이미지 스크랲 미용실에 추가
        designer_scarped_salon_objects = [DesignerScrapedSalon(salon_id=salon.id) for salon in salon_objects]
        image_scarped_salon_objects = [ImageScrapedSalon(salon_id=salon.id) for salon in salon_objects]

        self.db.add_all(designer_scarped_salon_objects)
        self.db.add_all(image_scarped_salon_objects)

        self.db.commit()
        return len(salon_objects)

    def get_existing_naver_ids_from(self, naver_ids: List[int]):
        return self.db.query(Salon.naver_place_id).filter(Salon.naver_place_id.in_(naver_ids)).all()
