from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker



engine=create_engine('sqlite:///restaurants.db', echo=True)

# create session
session=sessionmaker(bind=engine)()

Base=declarative_base()


def run_migration():
    Base.metadata.create_all(engine)