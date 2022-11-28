import typing as t
from abc import ABC, abstractmethod
import datetime
from uuid import uuid4

from ...models.inbounds import Sniffing
from ...models.inbounds import Client, Setting
from ...models.inbounds import TlsSettings, WsSettings, StreamSettings

from ...database.schemas import InboundsBase

from ...constants import time_info
from ...constants import byte_size


_ExpiryTime = t.Union[int, str, datetime.datetime, datetime.timedelta, time_info.Time, time_info.TimeUnit]
_ByteSize = t.Union[int, str, byte_size.Size, byte_size.SizeUnit]


def _convert_expiry_time(expiry_time: _ExpiryTime) -> int:
    now = datetime.datetime.now()

    if isinstance(expiry_time, datetime.datetime):
        expiry_time = expiry_time.timestamp()
    elif isinstance(expiry_time, datetime.timedelta):
        expiry_time = (now + expiry_time).timestamp()
    elif isinstance(expiry_time, int):
        pass
    elif isinstance(expiry_time, time_info.Time):
        expiry_time = now.timestamp() + expiry_time.seconds
    elif isinstance(expiry_time, time_info.TimeUnit):
        expiry_time = now.timestamp() + expiry_time.seconds
    elif isinstance(expiry_time, str):
        try:
            expiry_time = int(expiry_time)
        except ValueError:
            try:
                expiry_time = time_info.TimeUnit(expiry_time).seconds
            except ValueError:
                try:
                    expiry_time = time_info.from_string(expiry_time).seconds
                except ValueError:
                    raise ValueError("expiry_time is not a valid time format")
    else:
        raise ValueError(
            f"Invalid expiry_time: {expiry_time}\n"
            f"Expected {_ExpiryTime} but got {type(expiry_time)}"
        )

    if expiry_time < now.timestamp():
        expiry_time = expiry_time + now.timestamp()

    if expiry_time < 10000000000:
        expiry_time = expiry_time * 1000

    return expiry_time


def _convert_size(size: _ByteSize) -> int:
    if isinstance(size, int):
        pass
    elif isinstance(size, str):
        try:
            size = int(size)
        except ValueError:
            try:
                size = byte_size.SizeUnit(size).bytes
            except ValueError:
                try:
                    size = byte_size.from_string(size).bytes
                except ValueError:
                    raise ValueError("up is not a valid time format")
    elif isinstance(size, byte_size.Size):
        size = size.bytes
    elif isinstance(size, byte_size.SizeUnit):
        size = size.bytes
    else:
        raise ValueError(
            f"Invalid up: {size}\n"
            f"Expected {_ByteSize} but got {type(size)}"
        )

    return size


class Builder(ABC):
    @abstractmethod
    def build(self):
        ...

    def check(self):
        for k, v in self.__dict__.items():
            if v is None:
                raise ValueError(f"{k} is None")


class SniffingBuilder(Builder):
    def __init__(self):
        self._dest_override = None
        self._enabled = None

    def with_dest_override(self, dest_override: list[str]):
        self._dest_override = dest_override
        return self

    def with_enabled(self, enabled: bool):
        self._enabled = enabled
        return self

    def build(self) -> Sniffing:
        self.check()
        return Sniffing(destOverride=self._dest_override, enabled=self._enabled)


class SettingBuilder(Builder):
    def __init__(self):
        self._clients = None
        self._disable_insecure_encryption = None

    def with_clients(self, clients: list[Client]):
        self._clients = clients
        return self

    def with_disable_insecure_encryption(self, disable_insecure_encryption: bool):
        self._disable_insecure_encryption = disable_insecure_encryption
        return self

    def build(self) -> Setting:
        self.check()
        return Setting(clients=self._clients, disableInsecureEncryption=self._disable_insecure_encryption)


class StreamSettingBuilder(Builder):
    def __init__(self):
        self._network = None
        self._security = None
        self._tls_settings = None
        self._ws_settings = None

    def with_network(self, network: t.Literal["ws", "tcp", "kcp", "quic", "http", "grpc"]):
        self._network = network
        return self

    def with_security(self, security: str):
        self._security = security
        return self

    def with_tls_settings(self, tls_settings: TlsSettings):
        self._tls_settings = tls_settings
        return self

    def with_ws_settings(self, ws_settings: WsSettings):
        self._ws_settings = ws_settings
        return self

    def build(self) -> StreamSettings:
        self.check()
        return StreamSettings(
            network=self._network,
            security=self._security,
            tlsSettings=self._tls_settings,
            wsSettings=self._ws_settings,
        )


class InboundBuilder(Builder):
    def __init__(self):
        self._user_id = None
        self._up = None
        self._down = None
        self._total = None
        self._remark = None
        self._enable = None
        self._expiry_time = None
        self._listen = None
        self._port = None
        self._protocol = None
        self._settings = None
        self._stream_settings = None
        self._tag = None
        self._sniffing = None

    def with_user_id(self, user_id: int):
        self._user_id = user_id
        return self

    def with_up(self, up: _ByteSize):
        self._up = _convert_size(up)
        return self

    def with_down(self, down: _ByteSize):
        self._down = _convert_size(down)
        return self

    def with_total(self, total: int):
        self._total = total
        return self

    def with_remark(self, remark: str):
        self._remark = remark
        return self

    def with_enable(self, enable: bool):
        self._enable = enable
        return self

    def with_expiry_time(self, expiry_time: _ExpiryTime):
        self._expiry_time = _convert_expiry_time(expiry_time)
        return self

    def with_listen(self, listen: str):
        self._listen = listen
        return self

    def with_port(self, port: int):
        self._port = port
        return self

    def with_protocol(
            self, protocol: t.Literal["vmess", "vless", "trojan", "socks", "http", "shadowsocks", "dokodemo-door"]
    ):
        self._protocol = protocol
        return self

    def with_settings(self, settings: Setting):
        self._settings = settings.json()
        return self

    def with_stream_settings(self, stream_settings: StreamSettings):
        self._stream_settings = stream_settings.json()
        return self

    def with_tag(self, tag: str):
        self._tag = tag
        return self

    def with_sniffing(self, sniffing: Sniffing):
        self._sniffing = sniffing.json()
        return self

    def build(self) -> InboundsBase:
        self.check()
        return InboundsBase(
            user_id=self._user_id,
            up=self._up,
            down=self._down,
            total=self._total,
            remark=self._remark,
            enable=self._enable,
            expiry_time=self._expiry_time,
            listen=self._listen,
            port=self._port,
            protocol=self._protocol,
            settings=self._settings,
            stream_settings=self._stream_settings,
            tag=self._tag,
            sniffing=self._sniffing,
        )


class EasyInboundBuilder(Builder):
    def __init__(self):
        self._user_id = None
        self._up = None
        self._down = None
        self._total = None
        self._remark = None
        self._enable = None
        self._expiry_time = None
        self._listen = None
        self._port = None
        self._protocol = None
        self._settings = None
        self._network = None
        self._security = None
        self._server_name = None
        self._ws_path = None
        self._tag = None
        self._sniffing = None

    def with_user_id(self, user_id: int):
        self._user_id = user_id
        return self

    def with_up(self, up: _ByteSize):
        self._up = _convert_size(up)
        return self

    def with_down(self, down: _ByteSize):
        self._down = _convert_size(down)
        return self

    def with_total(self, total: int):
        self._total = total
        return self

    def with_remark(self, remark: str):
        self._remark = remark
        return self

    def with_enable(self, enable: bool):
        self._enable = enable
        return self

    def with_expiry_time(self, expiry_time: _ExpiryTime):
        self._expiry_time = _convert_expiry_time(expiry_time)
        return self

    def with_listen(self, listen: str):
        self._listen = listen
        return self

    def with_port(self, port: int):
        self._port = port
        return self

    def with_protocol(
            self, protocol: t.Literal["vmess", "vless", "trojan", "socks", "http", "shadowsocks", "dokodemo-door"]
    ):
        self._protocol = protocol
        return self

    def with_uuid(self, uuid: t.Union[str, uuid4] = uuid4()):
        _client = Client(id=uuid)
        self._settings = Setting(clients=[_client]).json()
        return self

    def with_network(self, network: t.Literal["ws", "tcp", "kcp", "quic", "http", "grpc"]):
        self._network = network
        return self

    def with_security(self, security: str):
        self._security = security
        return self

    def with_server_name(self, server_name: str):
        self._server_name = server_name
        return self

    def with_ws_path(self, ws_path: str):
        self._ws_path = ws_path
        return self

    def with_tag(self, tag: str):
        self._tag = tag
        return self

    def with_sniffing(self, sniffing: bool):
        self._sniffing = sniffing
        return self

    def build(self) -> InboundsBase:
        self.check()
        return InboundsBase(
            user_id=self._user_id,
            up=self._up,
            down=self._down,
            total=self._total,
            remark=self._remark,
            enable=self._enable,
            expiry_time=self._expiry_time,
            listen=self._listen,
            port=self._port,
            protocol=self._protocol,
            settings=self._settings,
            stream_settings=StreamSettings(
                network=self._network,
                security=self._security,
                tlsSettings=TlsSettings(serverName=self._server_name),
                wsSettings=WsSettings(path=self._ws_path),
            ).json(),
            tag=self._tag,
            sniffing=Sniffing(enabled=self._sniffing).json(),
        )
