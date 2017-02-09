from sqlalchemy import Column, Integer, String
from database import Base

class Widget(Base):
    __tablename__ = 'widgets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    url = Column(String(500))

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
        }
