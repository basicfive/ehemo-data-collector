from sqlalchemy.orm import Session
from typing import List

from app.schemas.designer import DesignerCreate
from app.models.designer import Designer

class DesignerService:
    def __init__(self, db: Session):
        self.db = db

    def create_designers(self, designers: List[DesignerCreate]):
        existing_insta_ids = self.get_existing_insta_ids_from([designer.insta_id for designer in designers])
        new_designers = [designer for designer in designers if designer.insta_id not in existing_insta_ids]

        designer_objects = [Designer(**designer.model_dump()) for designer in new_designers]
        self.db.add_all(designer_objects)
        self.db.commit()

        return len(designer_objects)

    def get_existing_insta_ids_from(self, insta_ids: List[str]) -> List[str]:
        return self.db.query(Designer.insta_id).filter(Designer.insta_id.in_(insta_ids)).all() # type: ignore
