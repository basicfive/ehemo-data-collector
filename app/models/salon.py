from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship
from app.models.base_model import TimeStampModel

class Salon(TimeStampModel):
    __tablename__ = "salons"
    naver_place_id = Column(Integer, unique=True, nullable=False, index=True)
    name = Column(String(40), nullable=False, index=True)

    designer = relationship("Designer", back_populates="salon")
    image_scraped_salon = relationship("ImageScrapedSalon", back_populates="salon")
    designer_scraped_salon = relationship("DesignerScrapedSalon", back_populates="salon")

