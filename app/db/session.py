from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url_object = URL.create(
#     'postgresql',
#     username='postgres',
#     password='kopkop99',
#     host='localhost',
#     # port=5432,
#     database='app',
# )

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:kopkop99@localhost/app-db"

# SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/MaxDroN/python_projects/const_data_books/readings_.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


Base.metadata.create_all(bind=engine)
