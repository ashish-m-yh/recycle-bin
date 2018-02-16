# coding: utf-8
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

import db_base

Base = declarative_base()
metadata = Base.metadata

class Industry(Base):
    __tablename__ = 'industry'

    id = Column(Integer, primary_key=True)
    industry = Column(String(255), nullable=False)

    t_industry_waste = Table(
        'industry_waste', metadata,
        Column('industry_id', Integer, nullable=False),
        Column('waste', Text, nullable=False),
        Column('waste_id', Integer, nullable=False)
    )

    def get_wastes(self):
        filter_column = self.t_industry_waste.columns['industry_id']
        return db_base.session.query(self.t_industry_waste.c.waste).filter(filter_column == self.id).all()

    @staticmethod
    def get_all_industry():
        rs = db_base.session.query(Industry).all()
        return rs

    @staticmethod
    def get_by_id(ind_id):
        return db_base.session.query(Industry).filter(Industry.id == ind_id).first()
