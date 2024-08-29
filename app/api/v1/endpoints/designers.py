from fastapi import APIRouter
from fastapi import Depends
from typing import List

from app.api.dependencies import get_designer_service
from app.schemas.designer import DesignerCreate
from app.services.designer_service import DesignerService

router = APIRouter()

@router.post("/create", response_model=int)
def create_designers(
        designers: List[DesignerCreate],
        service: DesignerService = Depends(get_designer_service)
):
    return service.create_designers(designers)