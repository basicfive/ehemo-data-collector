from fastapi import APIRouter
from typing import List
from fastapi import Depends

from app.schemas.naver_map_searched_url import NaverMapSearchedUrlCreate, NaverMapSearchedUrlInDB
from app.schemas.salon import SalonCreate
from app.api.dependencies import get_salon_service, get_naver_url_service
from app.services.naver_map_url_service import NaverMapUrlService
from app.services.salon_service import SalonService

router = APIRouter()

@router.post("/create-salon/batch")
def create_salon_batch_endpoint(
        salons: List[SalonCreate],
        service: SalonService = Depends(get_salon_service)
):
    created_count = service.create_salons(salons)
    return {"message": f"{created_count} salons created successfully"}

@router.get("/url/check-previously-used")
def check_previously_used(
        naver_map_url: str,
        service: NaverMapUrlService = Depends(get_naver_url_service)
):
    return service.is_url_previously_used(naver_map_url)

@router.post("/url/add-previously-used", response_model=NaverMapSearchedUrlInDB)
def add_previously_used(
        used: NaverMapSearchedUrlCreate,
        service: NaverMapUrlService = Depends(get_naver_url_service)
):
    return service.add_previously_used(used)