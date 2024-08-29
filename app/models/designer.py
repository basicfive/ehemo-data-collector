from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base_model import TimeStampModel
from app.enums.designer_positions import DesignerPositions

class Designer(TimeStampModel):
    __tablename__ = "designers"
    salon_id = Column(Integer, ForeignKey("salons.id"))
    insta_id = Column(String(20), nullable=False, index=True)
    name = Column(String(20), nullable=False)
    position = Column(String(20), nullable=False, default=DesignerPositions.DESIGNER)
    dm_sent = Column(Boolean, nullable=False, default=False)

    salon = relationship("Salon", back_populates="designer")

