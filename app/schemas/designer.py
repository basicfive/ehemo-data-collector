from pydantic import BaseModel

from app.enums.designer_positions import DesignerPositions

class DesignerCreate(BaseModel):
    salon_id: int
    insta_id: str
    name: str
    position: DesignerPositions

