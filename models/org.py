# coding: utf-8
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import db_base

Base = declarative_base()
metadata = Base.metadata


class Organization(UserMixin, Base):
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

    def set_password(self, password):
        self.passwd = generate_password_hash(password)

    def update(self):
        db_base.session.commit()

    def check_password(self, password):
        return check_password_hash(self.passwd, password)

    def get_waste(self, waste_type):
        table_name = "org_waste_gen" if waste_type == "generated" else "org_waste_req"
        cursor = db_base.conn.execute("SELECT * FROM " + table_name + " WHERE org_id=" + str(self.org_id)).cursor
        waste_list = []
        for row in cursor:
            _id, waste_id, quantity, unit = row
            waste_list.append({
                "waste_id": waste_id,
                "quantity": quantity,
                "unit": unit
            })
        return waste_list

    def reset_waste(self, waste_type):
        table_name = "org_waste_gen" if waste_type == "generated" else "org_waste_req"
        db_base.conn.execute("DELETE FROM " + table_name + " WHERE org_id=" + str(self.org_id))

    def update_waste(self, waste_req_list, waste_gen_list):
        self.reset_waste("generated")
        self.reset_waste("required")
        for waste_gen in waste_gen_list:
            db_base.conn.execute(
                self.t_org_waste_gen.insert().values(org_id=self.org_id, waste_item=int(waste_gen[0]),
                                                     qty=int(waste_gen[1]), units=waste_gen[2])
            )

        for waste_req in waste_req_list:
            db_base.conn.execute(
                self.t_org_waste_req.insert().values(org_id=self.org_id, waste_item=int(waste_req[0]),
                                                     qty=int(waste_req[1]), units=waste_req[2])
            )

    def save(self, org_info, waste_req_list, waste_gen_list):
        db_base.session.add(org_info)
        db_base.session.commit()
        db_base.session.refresh(org_info)

        for waste_gen in waste_gen_list:
            db_base.conn.execute(
                org_info.t_org_waste_gen.insert().values(org_id=org_info.org_id, waste_item=int(waste_gen[0]),
                                                         qty=int(waste_gen[1]), units=waste_gen[2])
            )

        for waste_req in waste_req_list:
            db_base.conn.execute(
                org_info.t_org_waste_req.insert().values(org_id=org_info.org_id, waste_item=int(waste_req[0]),
                                                         qty=int(waste_req[1]), units=waste_req[2])
            )

        return org_info.org_id

    def get_id(self):
        return self.org_id

    @staticmethod
    def get(org_id):
        return db_base.session.query(Organization).filter(Organization.org_id == int(org_id)).first()

    @staticmethod
    def get_by_email(email):
        return db_base.session.query(Organization).filter(Organization.email == email).first()

    @staticmethod
    def login(email, password):
        org = db_base.session.query(Organization).filter(Organization.email == email).first()
        if org:
            org = org if org.check_password(password=password) else None
        return org

    def get_matching_waste_orgs(self, waste_type):
        waste_list = self.get_waste(waste_type)
        table_name = "org_waste_gen" if waste_type != "generated" else "org_waste_req"
        orgs = []
        for waste in waste_list:
            waste_id = waste["waste_id"]
            org_ids = []
            cursor = db_base.conn.execute("SELECT org_id FROM " + table_name + " WHERE waste_item=" + str(waste_id)).cursor
            for row in cursor:
                org_ids.append(row[0])
            for org_id in org_ids:
                org = Organization.get(org_id)
                if org:
                    orgs.append(org)

        return orgs
