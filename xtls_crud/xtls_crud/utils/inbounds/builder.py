import typing as t
from abc import ABC, abstractmethod
import datetime

from ...models.inbounds import Sniffing
from ...models.inbounds import Client, Setting
from ...models.inbounds import TlsSettings, WsSettings, StreamSettings

from ...database.schemas import InboundsBase


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
