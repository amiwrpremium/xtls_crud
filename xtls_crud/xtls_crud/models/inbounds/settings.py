from pydantic import BaseModel, UUID4


class Client(BaseModel):
    id: UUID4
    alterId: int


class Setting(BaseModel):
    clients: list[Client]
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
