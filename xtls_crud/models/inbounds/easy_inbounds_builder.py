import typing as t
from uuid import uuid4
from pydantic import BaseModel, UUID4, Field, HttpUrl
from random import random
from string import ascii_letters

from ...utils.builders.inbounds_builder import (
    _ExpiryTime,  # noqa
    _ByteSize,  # noqa
    _convert_size,  # noqa
    _convert_expiry_time,  # noqa
    time_info,
    byte_size,
)
from ...core.settings import settings


ProtocolsType = t.Literal["vmess", "vless", "trojan", "socks", "http", "shadowsocks", "dokodemo-door"]
NetworksType = t.Literal["ws", "tcp", "kcp", "quic", "http", "grpc"]


def _random_path(length: int) -> str:
    if length >= 7:
        raise ValueError("length must be less than 7")

    return '/' + "".join([ascii_letters[int(random() * len(ascii_letters))] for _ in range(length)])


class EasyBuilderSchema(BaseModel):
    user_id: t.Optional[int] = 1
    up: t.Optional[_ByteSize] = Field(
        100 * byte_size.GIGABYTE.bytes, title="Upload", gt=0, multiple_of=1,
        example="100GB", description="Upload (Byte) Default: 100GB")
    down: t.Optional[_ByteSize] = Field(
        100 * byte_size.GIGABYTE.bytes, title="Download", gt=0, multiple_of=1,
        example=100 * byte_size.GIGABYTE.bytes, description="Download (Byte) Default: 100GB")
    total: t.Optional[int] = Field(
        0, title="Total", example=0, description="Total", ge=0, multiple_of=1)
    remark: t.Optional[str] = Field(
        ..., title="Remark", max_length=255, min_length=1, strip_whitespace=True, regex=r'^[\w\-\s]+$',
        example="amiwrpremium", description="Name of this setting")
    enable: t.Optional[bool] = Field(
        True, title="Enable", example=True, description="Enable this setting")
    expiry_time: t.Optional[_ExpiryTime] = Field(
        1 * time_info.MONTH.seconds * 1000, title="Expiry Time", gt=0, multiple_of=1,
        example="1MO", description="Expiry Time (MILLISECONDS) Default: Never")
    listen: str = Field(
        "", title="Listen", max_length=255, min_length=1, strip_whitespace=True, regex=r'^[\w\-\s]+$',
        example="", description="Listen")
    port: int = Field(
        ..., title="Port", gt=0, multiple_of=1, le=65535,
        example=443, description="Port to bind")
    protocol: t.Optional[ProtocolsType] = Field(
        "vmess", title="Protocol",
        example="vmess", description="Protocol")
    uuid: t.Optional[UUID4] = Field(
        uuid4(), title="UUID",
        example=uuid4(), description="UUID")
    network: t.Optional[NetworksType] = Field(
        "ws", title="Network",
        example="ws", description="Network")
    security: t.Optional[str] = Field(
        "tls", title="Security",
        example="tls", description="Security")
    server_name: HttpUrl = Field(
        settings.SITE_URL, title="Server Name", strip_whitespace=True,
        example=settings.SITE_URL, description="Server Name")
    ws_path: t.Optional[str] = Field(
        _random_path(6), title="WS Path", max_length=7, min_length=7, strip_whitespace=True,
        example=_random_path(6), description="WebSocket Path")
    tag: int = Field(
        ..., title="Tag", gt=0, multiple_of=1,
        example=1, description="Tag")
    sniffing: t.Optional[bool] = Field(
        True, title="Sniffing", example=True, description="Sniffing")
