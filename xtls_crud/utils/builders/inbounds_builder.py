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


class Builder(ABC):
    @abstractmethod
    def build(self):
        ...

    def check(self):
        for k, v in self.__dict__.items():
            if v is None:
                raise ValueError(f"{k} is None")


class SniffingBuilder(Builder):
    """
    Sniffing Builder for Inbounds

    ```python title="Example"
    from xtls_crud.utils.builders.inbounds_builder import SniffingBuilder

    sniffing = SniffingBuilder().with_dest_override(["http", "tls"]).with_enabled(True).build()

    print(sniffing)
    ```

    ```shell title="Output"
    Sniffing(destOverride=['http', 'tls'], enabled=True)
    ```
    """

    def __init__(self):
        self._dest_override = None
        self._enabled = None

    def with_dest_override(self, dest_override: list[str]):
        """
        Add dest override to sniffing builder

        Args:
            dest_override (list[str]): Dest override

        Returns:
            SniffingBuilder (SniffingBuilder): Sniffing builder
        """

        self._dest_override = dest_override
        return self

    def with_enabled(self, enabled: bool):
        """
        Add enabled to sniffing builder

        Args:
            enabled (bool): Enabled

        Returns:
            SniffingBuilder (SniffingBuilder): Sniffing builder
        """

        self._enabled = enabled
        return self

    def build(self) -> Sniffing:
        """
        Build sniffing using given parameters

        Returns:
            Sniffing (Sniffing): Sniffing

        Raises:
            ValueError: If any parameter is None
        """

        self.check()
        return Sniffing(destOverride=self._dest_override, enabled=self._enabled)


class SettingBuilder(Builder):
    """
    Setting Builder for Inbounds

    ```python title="Example"
    from xtls_crud.utils.builders.inbounds_builder import SettingBuilder

    setting = SettingBuilder().with_clients([Client(id="d36b31f0-44de-4576-a254-27d1d9410997", alterId=0)]).with_disable_insecure_encryption(True).build()

    print(setting)
    ```

    ```shell title="Output"
    Setting(clients=[Client(id='d36b31f0-44de-4576-a254-27d1d9410997', alterId=0)], disableInsecureEncryption=True)
    ```
    """

    def __init__(self):
        self._clients = None
        self._disable_insecure_encryption = None

    def with_clients(self, clients: list[Client]):
        """
        Add clients to setting builder

        Args:
            clients (list[Client]): Clients

        Returns:
            SettingBuilder (SettingBuilder): Setting builder
        """

        self._clients = clients
        return self

    def with_disable_insecure_encryption(self, disable_insecure_encryption: bool):
        """
        Add disable insecure encryption to setting builder

        Args:
            disable_insecure_encryption (bool): Disable insecure encryption

        Returns:
            SettingBuilder (SettingBuilder): Setting builder
        """

        self._disable_insecure_encryption = disable_insecure_encryption
        return self

    def build(self) -> Setting:
        """
        Build setting using given parameters

        Returns:
            Setting (Setting): Setting

        Raises:
            ValueError: If any parameter is None
        """

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
        self._up = byte_size.from_string(up)
        return self

    def with_down(self, down: _ByteSize):
        self._down = byte_size.from_string(down)
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
        self._expiry_time = time_info.from_string(expiry_time)
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
    """
    Easy Inbound Builder for Inbounds

    ```python title="Example"
    from xtls_crud.utils.builders.inbounds_builder import EasyInboundBuilder

    inbound = EasyInboundBuilder().with_user_id(1).with_up("1gb").with_down("1gb").with_total(
        0).with_remark("TEST").with_enable(True).with_expiry_time(
        "1D").with_listen(" ").with_port(1234).with_protocol("vmess").with_uuid(uuid4()).with_network(
        "ws").with_security("tls").with_server_name("v2ray.my-site.com").with_ws_path(
        "/test").with_tag("inbound-49428").with_sniffing(True).build()

    print(inbound)
    ```

    ```shell title="Output"
    InboundsBase(user_id=1, up='1gb', down='1gb', total=0, remark='TEST', enable=True, expiry_time=TimeInfo(time=1, unit='D'), listen=' ', port=1234, protocol='vmess', settings='{"clients": [{"id": "b1b1b1b1-b1b1-b1b1-b1b1-b1b1b1b1b1b1"}]}', stream_settings='{"network": "ws", "security": "tls", "tlsSettings": {"serverName": "v2ray.my-site.com"}, "wsSettings": {"path": "/test"}}', tag='inbound-49428', sniffing='{"enabled": true}')
    ```
    """

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
        """
        Add user id to inbound builder

        Args:
            user_id (int): User id

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._user_id = user_id
        return self

    def with_up(self, up: _ByteSize):
        """
        Add up to inbound builder

        Args:
            up (Union[int, str, datetime.datetime, datetime.timedelta, time_info.Time, time_info.TimeUnit]): Up

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._up = byte_size.from_string(up)
        return self

    def with_down(self, down: _ByteSize):
        """
        Add down to inbound builder

        Args:
            down (Union[int, str, datetime.datetime, datetime.timedelta, time_info.Time, time_info.TimeUnit]): Down

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder

        """
        self._down = byte_size.from_string(down)
        return self

    def with_total(self, total: int):
        """
        Add total to inbound builder

        Args:
            total (int): Total

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._total = total
        return self

    def with_remark(self, remark: str):
        """
        Add remark to inbound builder

        Args:
            remark (str): Remark

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._remark = remark
        return self

    def with_enable(self, enable: bool):
        """
        Add enable to inbound builder

        Args:
            enable (bool): Enable

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._enable = enable
        return self

    def with_expiry_time(self, expiry_time: _ExpiryTime):
        """
        Add expiry time to inbound builder

        Args:
            expiry_time (Union[int, str, datetime.datetime, datetime.timedelta, time_info.Time, time_info.TimeUnit]): Expiry time

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._expiry_time = time_info.from_string(expiry_time)
        return self

    def with_listen(self, listen: str):
        """
        Add listen to inbound builder

        Args:
            listen (str): Listen

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._listen = listen
        return self

    def with_port(self, port: int):
        """
        Add port to inbound builder

        Args:
            port (int): Port

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._port = port
        return self

    def with_protocol(
            self, protocol: t.Literal["vmess", "vless", "trojan", "socks", "http", "shadowsocks", "dokodemo-door"]
    ):
        """
        Add protocol to inbound builder

        Args:
            protocol (Literal["vmess", "vless", "trojan", "socks", "http", "shadowsocks", "dokodemo-door"]): Protocol

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._protocol = protocol
        return self

    def with_uuid(self, uuid: t.Union[str, uuid4] = uuid4()):
        """
        Add uuid to inbound builder

        Args:
            uuid (Union[str, uuid4], optional): Uuid. Defaults to uuid4().

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        _client = Client(id=uuid)
        self._settings = Setting(clients=[_client]).json()
        return self

    def with_network(self, network: t.Literal["ws", "tcp", "kcp", "quic", "http", "grpc"]):
        """
        Add network to inbound builder

        Args:
            network (Literal["ws", "tcp", "kcp", "quic", "http", "grpc"]): Network

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._network = network
        return self

    def with_security(self, security: str):
        """
        Add security to inbound builder

        Args:
            security (str): Security

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._security = security
        return self

    def with_server_name(self, server_name: str):
        """
        Add server name to inbound builder

        Args:
            server_name (str): Server name

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._server_name = server_name
        return self

    def with_ws_path(self, ws_path: str):
        """
        Add ws path to inbound builder

        Args:
            ws_path (str): Ws path

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._ws_path = ws_path
        return self

    def with_tag(self, tag: str):
        """
        Add tag to inbound builder

        Args:
            tag (str): Tag

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._tag = tag
        return self

    def with_sniffing(self, sniffing: bool):
        """
        Add sniffing to inbound builder

        Args:
            sniffing (bool): Sniffing

        Returns:
            EasyInboundBuilder (EasyInboundBuilder): Inbound builder
        """

        self._sniffing = sniffing
        return self

    def build(self) -> InboundsBase:
        """
        Build inbound

        Returns:
            InboundsBase (InboundsBase): Inbound

        Raises:
            ValueError: If any parameter is None
        """

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
