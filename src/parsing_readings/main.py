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


@app.get("/readings/", response_model=list[schemas.Reading])
def read_readings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    readings: list[models.Reading] = crud.get_readings(db, skip=skip, limit=limit)
    return readings


# @app.get("/readings/{reading_id}", response_model=schemas.Reading)
# def read_reading(reading_id: int, db: Session = Depends(get_db)):
#     db_reading = crud.get_reading(db, reading_id=reading_id)
#     if db_reading is None:
#         raise HTTPException(status_code=404, detail="Reading not found")
#     return db_reading

@app.post("/readings/", response_model=schemas.Reading)
def create_reading(date_id: int, zachalo_id: int, db: Session = Depends(get_db)):
    return crud.create_reading(db=db, date_id=date_id, zachalo_id=zachalo_id)


@app.get("/zachalos/", response_model=list[schemas.Zachalo])
def read_zachalos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zachalos: list[models.Zachalo] = crud.get_zachalos(db, skip=skip, limit=limit)
    return zachalos


@app.post("/zachalos/", response_model=schemas.Zachalo)
def create_zachalo(book_id: int, zachalo: schemas.ZachaloCreate,
                   db: Session = Depends(get_db)
                   ):
    return crud.create_zachalo(db=db, book_id=book_id, zachalo=zachalo)


@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)
                ):
    return crud.create_book(db=db, book=book)


# ТУТ ЗАГЛОХ Т.К ТРЕБУЕТСЯ ПРОВЕРКА ПО ДВУМ ПОЛЯМ (КАК Я ПОНЯЛ)
# @app.get("/periods/{num}/weeks/{sunday_num}/dates", response_model=list[schemas.Date])
# def read_dates(num: int, sunday_num: int, db: Session = Depends(get_db)):
#     dates: list[models.Date] = crud.get_dates_by_week(db, sunday_num=sunday_num)
#     return dates


# @app.get("/periods/{num}/weeks/{sunday_num}/dates/", response_model=schemas.Week)
# def read_week(num: int, sunday_num: int, db: Session = Depends(get_db)):
#     week: models.Week = crud.get_week(db, sunday_num=sunday_num, period_id=crud.get_period(db, num=num).id)
#     return week


# @app.post("/dates/", response_model=schemas.Date)
# def create_date(week_id: int, date: schemas.DateCreate, db: Session = Depends(get_db)
#                 ):
#     return crud.create_date(db=db, week_id=week_id, date=date)


# ПО МОЕМУ БЕЗСМЫСЛЕНЫЙ ПУТЬ, почти дублирует содержимое пути "/periods/", только без вывода инфо об periods
# @app.get("/periods/weeks", response_model=list[schemas.Week])
# def read_weeks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     weeks: list[models.Week] = crud.get_weeks(db, skip=skip, limit=limit)
#     return weeks


@app.get("/periods/{num}/weeks", response_model=list[schemas.Week])
def read_weeks(num: int, db: Session = Depends(get_db)):
    weeks: list[models.Week] = crud.get_weeks_by_period(db, period_id=crud.get_period(db, num=num).id)
    return weeks


# Подробнее тут: https://fastapi.tiangolo.com/tutorial/path-params/
# Не забыть про Enum для Литургия/Утреня/..


@app.get("/periods/{num}/weeks/{sunday_num}", response_model=schemas.Week)
def read_week(num: int, sunday_num: int, db: Session = Depends(get_db)):
    week: models.Week = crud.get_week(db, sunday_num=sunday_num, period_id=crud.get_period(db, num=num).id)
    return week


@app.post("/periods/{num}/weeks", response_model=schemas.Week)
def create_week(num: int, week: schemas.WeekCreate, db: Session = Depends(get_db)
                ):
    return crud.create_week(db=db, period_id=crud.get_period(db, num=num).id, week=week)


@app.get("/periods", response_model=list[schemas.Period])
def read_periods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    periods: list[models.Period] = crud.get_periods(db, skip=skip, limit=limit)
    return periods


@app.get("/periods/{num}", response_model=schemas.Period)
def read_period(num: int, db: Session = Depends(get_db)):
    period: models.Period = crud.get_period(db, num=num)
    return period


@app.post("/periods", response_model=schemas.Period)
def create_period(period: schemas.PeriodCreate, db: Session = Depends(get_db)
                  ):
    return crud.create_period(db=db, period=period)
