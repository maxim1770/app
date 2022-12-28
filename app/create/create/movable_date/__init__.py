from datetime import datetime
from pathlib import Path

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import schemas, crud, models
from app.api import deps


def create(num: schemas.CycleEnum):
    db: Session = deps.get_db().__next__()

    cycle: models.Cycle = crud.get_cycle(db, num)

    cycle_: schemas.Cycle = schemas.Cycle(weeks=cycle.weeks, num=cycle.num, title=cycle.title, id=cycle.id,
                                          encodings='utf-8')

    path: Path = Path(f'compare/date_{num}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json')
    path.write_text(cycle_.json(), encoding="utf-8")


class Zachalos(BaseModel):
    __root__: list[schemas.Zachalo]


def create_zachalo():
    db: Session = deps.get_db().__next__()

    zachalos: Zachalos = Zachalos.parse_obj(crud.get_all_zachalos(db))

    path: Path = Path(f'compare/zachalo_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json')
    path.write_text(zachalos.json(), encoding="utf-8")


def compare_zachalos():
    files = list(Path('compare').glob(f'zachalo_*.json'))

    z_1 = Zachalos.parse_file(files[0])
    z_2 = Zachalos.parse_file(files[1])

    assert z_1 == z_2
    print(True)


def compare(num: schemas.CycleEnum):
    files = list(Path('compare').glob(f'date_{num}*.json'))

    c_1 = schemas.Cycle.parse_file(files[0])
    c_2 = schemas.Cycle.parse_file(files[1])

    assert c_1 == c_2
    print(True)


if __name__ == '__main__':
    # create(schemas.CycleEnum.cycle_1)
    create_zachalo()
    # compare_zachalos()
    # compare(schemas.CycleEnum.cycle_3)
