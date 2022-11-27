import typing as t
from abc import ABC, abstractmethod
import datetime

from xtls_crud.xtls_crud.models.inbounds import Sniffing
from xtls_crud.xtls_crud.models.inbounds import Client, Setting
from xtls_crud.xtls_crud.models.inbounds import TlsSettings, WsSettings, StreamSettings

from xtls_crud.xtls_crud.database.schemas import InboundsBase

from xtls_crud.xtls_crud.constants import time_info


_ExpiryTime = t.Union[int, str, datetime.datetime, datetime.timedelta, time_info.Time, time_info.TimeUnit]


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

    def with_network(self, network: str):
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

    def with_up(self, up: int):
        self._up = up
        return self

    def with_down(self, down: int):
        self._down = down
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
        if isinstance(expiry_time, datetime.datetime):
            expiry_time = expiry_time.timestamp()
        elif isinstance(expiry_time, datetime.timedelta):
            expiry_time = (datetime.datetime.now() + expiry_time).timestamp()
        elif isinstance(expiry_time, int):
            pass
        elif isinstance(expiry_time, time_info.Time):
            expiry_time = expiry_time.seconds
        elif isinstance(expiry_time, time_info.TimeUnit):
            expiry_time = expiry_time.seconds
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

        self._expiry_time = expiry_time
        return self

    def with_listen(self, listen: str):
        self._listen = listen
        return self

    def with_port(self, port: int):
        self._port = port
        return self

    def with_protocol(self, protocol: str):
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
