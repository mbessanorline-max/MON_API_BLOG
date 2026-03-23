from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "mysql+pymysql://root@localhost:3306/blog"
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()