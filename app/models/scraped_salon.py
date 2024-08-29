from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import TimeStampModel

class ImageScrapedSalon(TimeStampModel):
    __tablename__ = "image_scraped_salons"
    salon_id = Column(Integer, ForeignKey("salons.id"))
    scrap_count = Column(Integer, default=0)

    salon = relationship("Salon", back_populates="image_scraped_salon")

class DesignerScrapedSalon(TimeStampModel):
    __tablename__ = "designer_scraped_salons"
    salon_id = Column(Integer, ForeignKey("salons.id"))
    scrap_count = Column(Integer, default=0)

    salon = relationship("Salon", back_populates="designer_scraped_salon")
