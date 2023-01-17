from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

url_object = URL.create(
    'postgresql',
    username='postgres',
    password='kopkop99',
    host='localhost',
    database='app-db',
)

engine = create_engine(url_object)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)
