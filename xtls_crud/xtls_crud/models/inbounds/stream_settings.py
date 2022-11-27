from pydantic import BaseModel, FilePath, validator


class Certificate(BaseModel):
    certificateFile: FilePath
    keyFile: FilePath


class TlsSettings(BaseModel):
    serverName: str
    certificates: list[Certificate]


class WsSettings(BaseModel):
    path: str
    headers: dict

    @validator('path')
    def path_must_start_with_slash(cls, v):
        if not v.startswith('/'):
            raise ValueError('path must start with /')
        return v


class StreamSettings(BaseModel):
    network: str
    security: str
    tlsSettings: TlsSettings
    wsSettings: WsSettings


if __name__ == '__main__':
    _sample = {
        "network": "ws",
        "security": "tls",
        "tlsSettings": {
            "serverName": "definitely-not-illegal.tech",
            "certificates": [
                {
                    "certificateFile": "/root/cert.crt",
                    "keyFile": "/root/private.key"
                }
            ]
        },
        "wsSettings": {
            "path": "/sajsa2",
            "headers": {}
        }
    }

    print(StreamSettings(**_sample))
