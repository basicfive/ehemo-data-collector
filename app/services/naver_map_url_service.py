from sqlalchemy.orm import Session

from app.models.naver_map_searched_url import NaverMapSearchedUrl
from app.schemas.naver_map_searched_url import NaverMapSearchedUrlCreate, NaverMapSearchedUrlInDB


class NaverMapUrlService:
    def __init__(self, db: Session):
        self.db = db

    def is_url_previously_used(self, url) -> bool:
        result = self.db.query(NaverMapSearchedUrl).filter(NaverMapSearchedUrl.url == url).first()
        return result is not None

    def add_previously_used(self, used: NaverMapSearchedUrlCreate):
        db_used = NaverMapSearchedUrl(**used.model_dump())
        self.db.add(db_used)
        self.db.commit()
        self.db.refresh(db_used)
        return db_used

