from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.base import SessionLocal
from app.services.designer_service import DesignerService
from app.services.naver_map_url_service import NaverMapUrlService
from app.services.salon_service import SalonService
from app.services.scraped_salon_service import ScrapedSalonService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_salon_service(db: Session = Depends(get_db)) -> SalonService:
    return SalonService(db)

def get_naver_url_service(db: Session = Depends(get_db)) -> NaverMapUrlService:
    return NaverMapUrlService(db)

def get_scraped_salon_service(db: Session = Depends(get_db)) -> ScrapedSalonService:
    return ScrapedSalonService(db)

def get_designer_service(db: Session = Depends(get_db)) -> DesignerService:
    return DesignerService(db)