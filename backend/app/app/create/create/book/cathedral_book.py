from sqlalchemy.orm import Session

from app import crud, schemas


def create_all_cathedral_books(db: Session) -> None:
    for cathedral in crud.cathedral.get_all(db):
        for rule_num in range(1, cathedral.num_rules + 1):
            cathedral_book_in = schemas.CathedralBookCreate(rule_num=rule_num)
            crud.create_cathedral_book(
                db,
                cathedral_slug=cathedral.slug,
                cathedral_book_in=cathedral_book_in
            )
