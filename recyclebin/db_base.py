from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from models import constants

Base = declarative_base()
engine = create_engine( "mysql://" + constants.DBUSER + ':' + constants.DBPASS + '@' + constants.DBHOST + '/' + constants.DBNAME)
conn = engine.connect()

session = Session(engine, expire_on_commit=False)
