from typing import List
from typing import Optional

from pydantic import BaseModel


class Sniffing(BaseModel):
    enabled: bool
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
