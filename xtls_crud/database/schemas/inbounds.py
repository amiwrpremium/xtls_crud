import typing as t
from pydantic import BaseModel


class InboundsBase(BaseModel):
    user_id: int
    up: int
    down: int
    total: int
    remark: str
    enable: bool
    expiry_time: int
    listen: str
    port: int
    protocol: str
    settings: str
    stream_settings: str
    tag: str
    sniffing: str


class InboundsOrderGetFilter(BaseModel):
    user_id: t.Optional[int] = None
    enable: t.Optional[bool] = None
    port: t.Optional[int] = None
    protocol: t.Optional[str] = None
    tag: t.Optional[str] = None


class InboundsCreate(InboundsBase):
    pass


class InboundsUpdate(InboundsBase):
    pass


class InboundsInDBBase(InboundsBase):
    id: t.Optional[int] = None

    class Config:
        orm_mode = True


class Inbounds(InboundsInDBBase):
    pass


class InboundsInDB(InboundsInDBBase):
    pass
