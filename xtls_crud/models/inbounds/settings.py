from uuid import uuid4
from typing import Optional
from typing import List
from typing import Union
from pydantic import BaseModel, UUID4, UUID1


class Client(BaseModel):
    id: Optional[Union[UUID4, UUID1]] = uuid4()
    alterId: Optional[int] = 0


class PrettyClient(Client):
    id: str
    alterId: int


class Setting(BaseModel):
    clients: List[Client]
    disableInsecureEncryption: Optional[bool] = False


class PrettySetting(Setting):
    clients: List[PrettyClient]
    disableInsecureEncryption: bool


if __name__ == '__main__':
    _sample = {
        "clients": [
            {
                "id": "438be03a-035f-44f4-a564-b30ff95442e3",
                "alterId": 0
            }
        ],
        "disableInsecureEncryption": False
    }

    print(Setting(**_sample))
