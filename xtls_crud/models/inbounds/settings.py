from uuid import uuid4
from typing import Optional
from typing import List
from pydantic import BaseModel, UUID4


class Client(BaseModel):
    id: Optional[UUID4] = uuid4()
    alterId: Optional[int] = 0


class Setting(BaseModel):
    clients: List[Client]
    disableInsecureEncryption: Optional[bool] = False


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
