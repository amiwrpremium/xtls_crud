"""
# Models for Inbounds Builder
Make it easy to build inbounds

"""

import typing as t
from uuid import uuid4
from pydantic import BaseModel, UUID4, UUID1, Field, HttpUrl
from random import random
from string import ascii_letters

from ...utils.builders.inbounds_builder import (
    _ExpiryTime,  # noqa
    _ByteSize,  # noqa
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


class EasyBuilderSchemaCreate(BaseModel):
    """
    Easy builder schema create

    Keyword Args:
        user_id (int): User ID
        up (int): Upload (Byte)
        down (int): Download (Byte)
        total (int): Total
        remark (str): Remark
        enable (bool): Enable
        expiry_time (int): Expiry Time (MILLISECONDS)
        listen (str): Listen
        port (int): Port
        protocol (str): Protocol
        uuid (str): UUID
        network (str): Network
        security (str): Security
        server_name (str): Server Name
        ws_path (str): WebSocket Path
        tag (int): Tag
        sniffing (bool): Sniffing

    Returns:
        EasyBuilderSchemaCreate (EasyBuilderSchemaCreate): Easy builder schema create
    """

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
    uuid: t.Optional[t.Union[UUID4, UUID1]] = Field(
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


class EasyBuilderSchemaUpdate(BaseModel):
    """
    Easy builder schema update

    Keyword Args:
        user_id (int): User ID (Default: None)
        up (int): Upload (Byte) (Default: None)
        down (int): Download (Byte) (Default: None)
        total (int): Total (Default: None)
        remark (str): Name of this setting (Default: None)
        enable (bool): Enable this setting (Default: None)
        expiry_time (int): Expiry Time (MILLISECONDS) (Default: None)
        listen (str): Listen (Default: None)
        port (int): Port to bind (Default: None)
        protocol (str): Protocol (Default: None)
        uuid (str): UUID (Default: None)
        network (str): Network (Default: None)
        security (str): Security (Default: None)
        server_name (str): Server Name (Default: None)
        ws_path (str): WebSocket Path (Default: None)
        tag (int): Tag (Default: None)
        sniffing (bool): Sniffing (Default: None)

    Returns:
        EasyBuilderSchemaUpdate (EasyBuilderSchemaUpdate): Easy builder schema update
    """

    user_id: t.Optional[int] = 1
    up: t.Optional[_ByteSize] = Field(
        None, title="Upload", gt=0, multiple_of=1,
        example="100GB", description="Upload (Byte) Default: 100GB")
    down: t.Optional[_ByteSize] = Field(
        None, title="Download", gt=0, multiple_of=1,
        example=100 * byte_size.GIGABYTE.bytes, description="Download (Byte) Default: 100GB")
    total: t.Optional[int] = Field(
        None, title="Total", example=0, description="Total", ge=0, multiple_of=1)
    remark: t.Optional[str] = Field(
        None, title="Remark", max_length=255, min_length=1, strip_whitespace=True, regex=r'^[\w\-\s]+$',
        example="amiwrpremium", description="Name of this setting")
    enable: t.Optional[bool] = Field(
        True, title="Enable", example=True, description="Enable this setting")
    expiry_time: t.Optional[_ExpiryTime] = Field(
        None, title="Expiry Time", gt=0, multiple_of=1,
        example="1MO", description="Expiry Time (MILLISECONDS) Default: Never")
    listen: str = Field(
        None, title="Listen", max_length=255, min_length=1, strip_whitespace=True, regex=r'^[\w\-\s]+$',
        example="", description="Listen")
    port: int = Field(
        None, title="Port", gt=0, multiple_of=1, le=65535,
        example=443, description="Port to bind")
    protocol: t.Optional[ProtocolsType] = Field(
        None, title="Protocol",
        example="vmess", description="Protocol")
    uuid: t.Optional[t.Union[UUID4, UUID1]] = Field(
        None, title="UUID",
        example=uuid4(), description="UUID")
    network: t.Optional[NetworksType] = Field(
        None, title="Network",
        example="ws", description="Network")
    security: t.Optional[str] = Field(
        None, title="Security",
        example="tls", description="Security")
    server_name: HttpUrl = Field(
        None, title="Server Name", strip_whitespace=True,
        example=settings.SITE_URL, description="Server Name")
    ws_path: t.Optional[str] = Field(
        None, title="WS Path", max_length=7, min_length=7, strip_whitespace=True,
        example=_random_path(6), description="WebSocket Path")
    tag: int = Field(
        None, title="Tag", gt=0, multiple_of=1,
        example=1, description="Tag")
    sniffing: t.Optional[bool] = Field(
        None, title="Sniffing", example=True, description="Sniffing")
