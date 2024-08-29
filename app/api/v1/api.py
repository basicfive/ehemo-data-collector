from fastapi import APIRouter
from app.api.v1.endpoints import salons, scrapers, designers

router = APIRouter()
router.include_router(salons.router, prefix="/salons", tags=["salons"])
router.include_router(scrapers.router, prefix="/scrapers", tags=["scrapers"])
router.include_router(designers.router, prefix="/designers", tags=["designers"])
