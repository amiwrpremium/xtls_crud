from uuid import uuid4
from typing import Optional
from typing import List
from typing import Union
from pydantic import BaseModel, UUID4, UUID1


class Client(BaseModel):
    """
    Client

    Keyword Args:
        id (Optional[Union[UUID4, UUID1]]): id (default: uuid4())
        alterId (Optional[int]): alterId (default: 0)

    Returns:
        Client (Client): Client
    """

    id: Optional[Union[UUID4, UUID1]] = uuid4()
    alterId: Optional[int] = 0


class PrettyClient(Client):
    """
    Pretty Client

    Keyword Args:
        id (str): id
        alterId (int): alterId

    Returns:
        PrettyClient (PrettyClient): Pretty Client
    """

    id: str
    alterId: int


class Setting(BaseModel):
    """
    Setting

    Keyword Args:
        clients (List[Client]): clients
        disableInsecureEncryption (Optional[bool]): disableInsecureEncryption (default: False)

    Returns:
        Setting (Setting): Setting
    """

    clients: List[Client]
    disableInsecureEncryption: Optional[bool] = False


class PrettySetting(Setting):
    """
    Pretty Setting

    Keyword Args:
        clients (List[PrettyClient]): clients
        disableInsecureEncryption (bool): disableInsecureEncryption

    Returns:
        PrettySetting (PrettySetting): Pretty Setting
    """

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
