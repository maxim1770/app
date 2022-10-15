from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/readings/", response_model=schemas.Reading)
def create_reading(reading: schemas.Reading, db: Session = Depends(get_db)):
    return crud.create_reading(db=db, reading=reading)

@app.get("/readings/", response_model=list[schemas.Reading])
def read_readings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    readings = crud.get_readings(db, skip=skip, limit=limit)
    return readings


@app.get("/readings/{reading_id}", response_model=schemas.Reading)
def read_reading(reading_id: int, db: Session = Depends(get_db)):
    db_reading = crud.get_reading(db, reading_id=reading_id)
    if db_reading is None:
        raise HTTPException(status_code=404, detail="Reading not found")
    return db_reading


@app.post("/readings/{reading_id}/dates/", response_model=schemas.Date)
def create_date_for_reading(
        reading_id: int, date: schemas.Date, db: Session = Depends(get_db)
):
    return crud.create_reading_date(db=db, date=date, reading_id=reading_id)


@app.get("/dates/", response_model=list[schemas.Date])
def read_dates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dates = crud.get_dates(db, skip=skip, limit=limit)
    return dates


@app.post("/readings/{reading_id}/books/", response_model=schemas.Book)
def create_book_for_reading(
        reading_id: int, book: schemas.Book, db: Session = Depends(get_db)
):
    return crud.create_reading_book(db=db, book=book, reading_id=reading_id)


@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books
