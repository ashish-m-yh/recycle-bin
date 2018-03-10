# coding: utf-8
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

import db_base

Base = declarative_base()
metadata = Base.metadata


class Waste(Base):
    __tablename__ = 'waste_master'

    waste_id = Column(Integer, primary_key=True)
    waste = Column(String(255), nullable=False)

    @staticmethod
    def get_all_waste():
        rs = db_base.session.query(Waste).all()
        return rs

    @staticmethod
    def get_by_id(waste_id):
        return db_base.session.query(Waste).filter(Waste.id == waste_id).first()
