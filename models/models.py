from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import constants

Base = declarative_base()
engine = create_engine( "mysql://" + constants.dbuser + ':' + constants.dbpass + '@' + constants.dbhost + '/' + constants.dbname)

session = Session(engine)
