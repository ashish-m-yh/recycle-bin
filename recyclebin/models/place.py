from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from recyclebin import db_base

Base = declarative_base()
metadata = Base.metadata


class Place(Base):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    pincode = Column(Integer, nullable=False)
    geocode = Column(Integer, nullable=False)
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)

    @staticmethod
    def get_all_places():
        places = db_base.session.query(Place).all()
        return places

    @staticmethod
    def get_by_id(place_id):
        return db_base.session.query(Place).filter(Place.id == place_id).first()
