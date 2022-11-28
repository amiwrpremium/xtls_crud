from typing import List
from typing import Optional

from pydantic import BaseModel


class Sniffing(BaseModel):
    enabled: Optional[bool] = True
    destOverride: Optional[List[str]] = ["http", "tls"]


if __name__ == '__main__':
    _sample = {
        "enabled": True,
        "destOverride": [
            "http",
            "tls"
        ]
    }

    print(Sniffing(**_sample))
