from typing import List, Optional, Dict
from pydantic import BaseModel, FilePath, validator


class Certificate(BaseModel):
    """
    Certificate

    Keyword Args:
        certificateFile (Optional[FilePath]): certificateFile (default: /root/cert.crt)
        keyFile (Optional[FilePath]): keyFile (default: /root/private.key)

    Returns:
        Certificate (Certificate): Certificate
    """

    certificateFile: Optional[FilePath] = "/root/cert.crt"
    keyFile: Optional[FilePath] = "/root/private.key"


class PrettyCertificate(BaseModel):
    """
    Pretty Certificate (Used for API)

    Keyword Args:
        certificateFile (str): certificateFile
        keyFile (str): keyFile

    Returns:
        PrettyCertificate (PrettyCertificate): Pretty Certificate
    """

    certificateFile: str
    keyFile: str


class TlsSettings(BaseModel):
    """
    TlsSettings

    Keyword Args:
        serverName (str): serverName
        certificates (Optional[List[Certificate]]): certificates (default: [Certificate()])

    Returns:
        TlsSettings (TlsSettings): TlsSettings
    """

    serverName: str
    certificates: Optional[List[Certificate]] = [Certificate()]


class PrettyTlsSettings(BaseModel):
    """
    Pretty TlsSettings (Used for API)

    Keyword Args:
        serverName (str): serverName
        certificates (Optional[List[PrettyCertificate]]): certificates (default: [PrettyCertificate()])

    Returns:
        PrettyTlsSettings (PrettyTlsSettings): Pretty TlsSettings
    """

    serverName: str
    certificates: List[PrettyCertificate]


class WsSettings(BaseModel):
    """
    WsSettings

    Keyword Args:
        path (str): path
        headers (Optional[Dict[str, str]]): headers (default: {})

    Returns:
        WsSettings (WsSettings): WsSettings
    """

    path: str
    headers: Optional[Dict[str, str]] = {}

    @validator('path')
    def path_must_start_with_slash(cls, v):
        if not v.startswith('/'):
            raise ValueError('path must start with /')
        return v


class StreamSettings(BaseModel):
    """
    StreamSettings

    Keyword Args:
        network (str): network
        security (str): security
        tlsSettings (TlsSettings): tlsSettings
        wsSettings (WsSettings): wsSettings

    Returns:
        StreamSettings (StreamSettings): StreamSettings
    """

    network: str
    security: str
    tlsSettings: TlsSettings
    wsSettings: WsSettings


class PrettyStreamSettings(BaseModel):
    """
    Pretty StreamSettings (Used for API)

    Keyword Args:
        network (str): network
        security (str): security
        tlsSettings (PrettyTlsSettings): tlsSettings
        wsSettings (WsSettings): wsSettings

    Returns:
        PrettyStreamSettings (PrettyStreamSettings): Pretty StreamSettings
    """

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
