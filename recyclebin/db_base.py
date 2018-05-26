from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import constants

Base = declarative_base()
engine = create_engine("mysql://" + constants.DBUSER + ':' + constants.DBPASS + '@' + constants.DBHOST + '/' + constants.DBNAME, pool_recycle=900)
conn = engine.connect()

session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
