from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from recyclebin import db_base

Base = declarative_base()
metadata = Base.metadata


class District(Base):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    @staticmethod
    def get_all_district():
        district = db_base.session.query(District).all()
        return district

    @staticmethod
    def get_by_id(district_id):
        return db_base.session.query(District).filter(District.id == district_id).first()
