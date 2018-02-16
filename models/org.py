# coding: utf-8
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

import db_base

Base = declarative_base()
metadata = Base.metadata


class Organization(Base):
    __tablename__ = 'organization'

    org_id = Column(Integer, primary_key=True)
    industry_id = Column(Integer, nullable=False)
    org_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    passwd = Column(String(255), nullable=False)
    contact_no1 = Column(String(10), nullable=False)
    contact_no2 = Column(String(10), nullable=False)
    address = Column(String, nullable=False)
    contact_person = Column(String(255), nullable=False)

    t_org_waste_gen = Table(
        'org_waste_gen', metadata,
        Column('org_id', Integer, nullable=False),
        Column('waste_item', Integer, nullable=False),
        Column('qty', Integer, nullable=False),
        Column('units', String(10), nullable=False)
    )

    t_org_waste_req = Table(
        'org_waste_req', metadata,
        Column('org_id', Integer, nullable=False),
        Column('waste_item', Integer, nullable=False),
        Column('qty', Integer, nullable=False),
        Column('units', String(10), nullable=False)
    )

    def save(org_info):
        result = db_base.session.execute(Organisation.__table__.insert(), org_info)
        org_id = result.inserted_primary_key[0]
        return org_id
