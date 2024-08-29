from fastapi import APIRouter
from fastapi import Depends
from app.api.dependencies import get_scraped_salon_service
from app.schemas.salon_dto import SalonsToUpdate, ScrapedSalonResponse

from app.services.scraped_salon_service import ScrapedSalonService

router = APIRouter()

# 디자이너 스크랲 아직 안한 미용실 정보 반환
@router.get("/get-designer-scraped-salon", response_model=ScrapedSalonResponse)
def get_designer_scraped_salon_urls(
        service:ScrapedSalonService = Depends(get_scraped_salon_service)
):
    return service.get_designer_scraped_salon_urls()

# 해당 리스트에 존재하는 salon들 모두 scrap count 하나 올려주기
@router.post("/update-designer-scraped-salon", response_model=int)
def update_designer_scraped_salon(
        salons_to_update: SalonsToUpdate,
        service: ScrapedSalonService = Depends(get_scraped_salon_service)
):
    return service.update_designer_scraped_salons(salons_to_update)

# 이미지 스크랲 아직 안한 미용실 정보 반환
@router.get("/get-image-scraped-salon", response_model=ScrapedSalonResponse)
def get_image_scraped_salon_urls(
        service:ScrapedSalonService = Depends(get_scraped_salon_service)
):
    return service.get_image_scraped_salon_urls()

# 해당 리스트에 존재하는 salon들 모두 scrap count 하나 올려주기
@router.post("/update-image-scraped-salon", response_model=int)
def update_image_scraped_salons(
        salons_to_update: SalonsToUpdate,
        service: ScrapedSalonService = Depends(get_scraped_salon_service)
):
    return service.update_image_scraped_salons(salons_to_update)

