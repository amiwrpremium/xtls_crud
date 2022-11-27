from pydantic import BaseModel


class Sniffing(BaseModel):
    enabled: bool
    destOverride: list[str]


if __name__ == '__main__':
    _sample = {
        "enabled": True,
        "destOverride": [
            "http",
            "tls"
        ]
    }

    print(Sniffing(**_sample))