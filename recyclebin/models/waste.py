# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from collections import Counter

from recyclebin import db_base

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
        return db_base.session.query(Waste).filter(Waste.waste_id == waste_id).first()

    @staticmethod
    def get_all_waste_in_system():
        table_names = ["org_waste_gen", "org_waste_req"]

        all_wastes = Waste.get_all_waste()
        waste_counter = Counter()

        for table in table_names:
            qry = "SELECT waste_item, qty from " + table
            cursor = db_base.conn.execute(qry).cursor
            for row in cursor:
                _id = row[0]
                waste = filter(lambda x: x.waste_id == _id, all_wastes)[0]
                waste_counter[waste.waste.title()] += row[1]

        return waste_counter
