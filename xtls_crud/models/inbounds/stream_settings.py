from typing import List, Optional, Dict
from pydantic import BaseModel, FilePath, validator


class Certificate(BaseModel):
    certificateFile: Optional[FilePath] = "/root/cert.crt"
    keyFile: Optional[FilePath] = "/root/private.key"


class PrettyCertificate(BaseModel):
    certificateFile: str
    keyFile: str


class TlsSettings(BaseModel):
    serverName: str
    certificates: Optional[List[Certificate]] = [Certificate()]


class PrettyTlsSettings(BaseModel):
    serverName: str
    certificates: List[PrettyCertificate]


class WsSettings(BaseModel):
    path: str
    headers: Optional[Dict[str, str]] = {}

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


class PrettyStreamSettings(BaseModel):
    network: str
    security: str
    tlsSettings: PrettyTlsSettings
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
