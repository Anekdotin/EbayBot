from sqlalchemy import Column, Integer, TEXT
from app import Base
from app import engine


class EbaySellers(Base):
    __tablename__ = "users"
    __bind_key__ = 'ebay_database_sellers'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(TEXT)


Base.metadata.create_all(engine)
