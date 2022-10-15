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
def create_reading(date_id: int, bible_zachalo_id: int, db: Session = Depends(get_db)):
    return crud.create_reading(db=db, date_id=date_id, bible_zachalo_id=bible_zachalo_id)


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


@app.post("/dates/", response_model=schemas.Date)
def create_date_for_reading(date: schemas.DateCreate, db: Session = Depends(get_db)
):
    return crud.create_reading_date(db=db, date=date)


@app.get("/dates/", response_model=list[schemas.Date])
def read_dates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dates = crud.get_dates(db, skip=skip, limit=limit)
    return dates


@app.post("/bible_zachalos/", response_model=schemas.BibleZachalo)
def create_bible_zachalo_for_reading(bible_zachalo: schemas.BibleZachaloCreate, db: Session = Depends(get_db)
                            ):
    return crud.create_reading_bible_zachalo(db=db, bible_zachalo=bible_zachalo)


@app.get("/bible_zachalos/", response_model=list[schemas.BibleZachalo])
def read_bible_zachalos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bible_zachalos = crud.get_bible_zachalos(db, skip=skip, limit=limit)
    return bible_zachalos
