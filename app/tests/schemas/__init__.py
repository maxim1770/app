from uuid import UUID
from pydantic import BaseModel


class User(BaseModel):
    id: UUID


if __name__ == '__main__':
    # u = User(id=UUID('cf57432e-809e-4353-adbd-9d5c0d733868'))
    # u2 = User(id='cf57432e-809e-4353-adbd-9d5c0d733868')
    u3 = User(id='59014138-46CC-4335-9E3C-9F903FD854A3')
    # print(u)
    # print(u2)
    print(u3)