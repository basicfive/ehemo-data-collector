from sqlalchemy import Column, String

from app.models.base_model import TimeStampModel

class NaverMapSearchedUrl(TimeStampModel):
    __tablename__ = "naver_map_searched_urls"
    url = Column(String(2083), nullable=False, index=True)
    search_keyword = Column(String(20), nullable=False, index=True)
