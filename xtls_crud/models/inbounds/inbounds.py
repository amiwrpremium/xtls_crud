from datetime import datetime
import json
from pydantic import BaseModel, validator


from .settings import PrettySetting as Setting
from .stream_settings import PrettyStreamSettings as StreamSettings
from .sniffing import Sniffing


class PrettyInbound(BaseModel):
    user_id: int
    up: int
    down: int
    total: int
    remark: str
    enable: bool
    expiry_time: datetime
    listen: str
    port: int
    protocol: str
    settings: Setting
    stream_settings: StreamSettings
    tag: str
    sniffing: Sniffing
    id: int

    class Config:
        orm_mode = True

    @validator('settings', pre=True)
    def validate_settings(cls, v):
        return Setting(**json.loads(v))

    @validator('stream_settings', pre=True)
    def validate_stream_settings(cls, v):
        return StreamSettings(**json.loads(v))

    @validator('sniffing', pre=True)
    def validate_sniffing(cls, v):
        return Sniffing(**json.loads(v))


if __name__ == '__main__':
    _sample = {
        "user_id": 1,
        "up": 0,
        "down": 0,
        "total": 23622320128,
        "remark": "testings1",
        "enable": True,
        "expiry_time": 1669836498529,
        "listen": "",
        "port": 49428,
        "protocol": "vmess",
        "settings": "{\n  \"clients\": [\n    {\n      \"id\": \"4bde567b-425a-4fb9-f03b-aa5cf7d02e51\",\n      \"alterId\": 0\n    }\n  ],\n  \"disableInsecureEncryption\": false\n}",
        "stream_settings": "{\n  \"network\": \"ws\",\n  \"security\": \"tls\",\n  \"tlsSettings\": {\n    \"serverName\": \"definitely-not-illegal.tech\",\n    \"certificates\": [\n      {\n        \"certificateFile\": \"/root/cert.crt\",\n        \"keyFile\": \"/root/private.key\"\n      }\n    ]\n  },\n  \"wsSettings\": {\n    \"path\": \"/ask21\",\n    \"headers\": {}\n  }\n}",
        "tag": "inbound-49428",
        "sniffing": "{\n  \"enabled\": true,\n  \"destOverride\": [\n    \"http\",\n    \"tls\"\n  ]\n}",
        "id": 1
    }

    print(PrettyInbound(**_sample))
