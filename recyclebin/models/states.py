from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base

from recyclebin import db_base

Base = declarative_base()
metadata = Base.metadata


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    @staticmethod
    def get_all_states():
        states = db_base.session.query(State).all()
        return states

    @staticmethod
    def get_by_id(state_id):
        return db_base.session.query(State).filter(State.id == state_id).first()
