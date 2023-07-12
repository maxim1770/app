from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.tests import test_utils


def _test_create_cycle(client: TestClient) -> None:
    cycle_in = test_utils.create_random_cycle_in()
    r = client.post(
        '/movable-dates',
        json=cycle_in.model_dump(),
    )
    assert 200 <= r.status_code < 300
    created_cycle = r.json()
    assert created_cycle['num'] == cycle_in.num
    assert 'id' in created_cycle


# def test_get_cycle_by_cycle_num_in_enum_bad(
#         client: TestClient, db: Session
# ) -> None:
#     '''По идее должно работать есть правильно написать функцию read_cycle
#     И там сделать проверку на None, и если значения нет в базе данных, то генерировать
#      raise HTTPException(status_code=404, detail="Item not found")
#      НО ВОЗМОЖНО В ЭТОЙ ФУНКЦИИ ЭТОГО И НЕ НАДО, ТК ПРОВЕРКУ НА ТО ЧТО БУДЕТ от [1, 3] дает CycleNum
#      А ЗНАЧНИЯ [1, 3] скорее всего будут в бд
#      (т.к их всего 3, и без них вообще ничего бы не работало, если бы их не было)
#     '''
#     r = client.get(
#         '/movable-dates/cycle-2'
#     )
#     assert r.status_code == 404
#     print(r.json())


def _test_get_cycle_by_cycle_num_bad(
        client: TestClient, db: Session
) -> None:
    r = client.get(
        '/movable-dates/cycle-0'
    )
    assert r.status_code == 422
    assert r.json() == {
        'detail': [{
            'loc': ['path', 'cycle_num'],
            'msg': 'value is not a valid enumeration member; permitted: 1, 2, 3',
            'type': 'type_error.enum', 'ctx': {'enum_values': [1, 2, 3]}
        }]
    }
