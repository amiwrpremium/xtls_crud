from typing import Optional
from pydantic import BaseModel


class InboundsBase(BaseModel):
    """
    Inbounds base schema

    Keyword Args:
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        InboundsBase (InboundsBase): Inbounds base schema

    Examples:
        ```py linenums="1" title="inbounds.py"
        from xtls_crud.database.schemas.inbounds import InboundsBase

        inbounds = InboundsBase(
            user_id=1,
            up=0,
            down=0,
            total=0,
            remark="remark",
            enable=True,
            expiry_time=0,
            listen=""
            port=0,
            protocol="",
            settings="",
            stream_settings="",
            tag="",
            sniffing="",
        )

        print(inbounds)
        ```

        ```shell title="Result"
        InboundsBase(user_id=1, up=0, down=0, total=0, remark='remark', enable=True, expiry_time=0, listen='', port=0, protocol='', settings='', stream_settings='', tag='', sniffing='')  # noqa: E501
        ```
    """

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
    """
    Inbounds get filter schema

    Keyword Args:
        user_id (Optional[int]): user id
        enable (Optional[bool]): enable
        port (Optional[int]): port
        protocol (Optional[str]): protocol
        tag (Optional[str]): tag

    Returns:
        InboundsOrderGetFilter (InboundsOrderGetFilter): Inbounds get filter schema

    Examples:
        ```py linenums="1" title="inbounds.py"
        from xtls_crud.database.schemas.inbounds import InboundsOrderGetFilter

        inbounds = InboundsOrderGetFilter(
            user_id=1,
            enable=True,
        )

        print(inbounds)
        ```

        ```shell title="Result"
        InboundsOrderGetFilter(user_id=1, enable=True, port=None, protocol=None, tag=None)
        ```
    """

    user_id: Optional[int] = None
    enable: Optional[bool] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    tag: Optional[str] = None


class InboundsCreate(InboundsBase):
    """
    Inbounds create schema

    Keyword Args:
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        InboundsCreate (InboundsCreate): Inbounds create schema

    Examples:
        ```py linenums="1" title="inbounds.py"
        from xtls_crud.database.schemas.inbounds import InboundsCreate

        inbounds = InboundsCreate(
            user_id=1,
            up=0,
            down=0,
            total=0,
            remark="remark",
            enable=True,
            expiry_time=0,
            listen=""
            port=0,
            protocol="",
            settings="",
            stream_settings="",
            tag="",
            sniffing="",
        )

        print(inbounds)
        ```

        ```shell title="Result"
        InboundsCreate(user_id=1, up=0, down=0, total=0, remark='remark', enable=True, expiry_time=0, listen='', port=0, protocol='', settings='', stream_settings='', tag='', sniffing='')  # noqa: E501
        ```
    """


class InboundsUpdate(InboundsBase):
    """
    Inbounds update schema

    Keyword Args:
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        InboundsUpdate (InboundsUpdate): Inbounds update schema

    Examples:
        ```py linenums="1" title="inbounds.py"
        from xtls_crud.database.schemas.inbounds import InboundsUpdate

        inbounds = InboundsUpdate(
            user_id=1,
            up=0,
            down=0,
            total=0,
            remark="remark",
            enable=True,
            expiry_time=0,
            listen=""
            port=0,
            protocol="",
            settings="",
            stream_settings="",
            tag="",
            sniffing="",
        )

        print(inbounds)
        ```

        ```shell title="Result"
        InboundsUpdate(user_id=1, up=0, down=0, total=0, remark='remark', enable=True, expiry_time=0, listen='', port=0, protocol='', settings='', stream_settings='', tag='', sniffing='')  # noqa: E501
        ```
    """


class InboundsInDBBase(InboundsBase):
    """
    Inbounds in database base schema

    Attributes:
        id (int): id
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        InboundsInDBBase (InboundsInDBBase): Inbounds in database base schema
    """

    id: Optional[int] = None

    class Config:
        orm_mode = True


class Inbounds(InboundsInDBBase):
    """
    Inbounds schema

    Attributes:
        id (int): id
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        Inbounds (Inbounds): Inbounds schema
    """


class InboundsInDB(InboundsInDBBase):
    """
    Inbounds in database schema

    Attributes:
        id (int): id
        user_id (int): user id
        up (int): up
        down (int): down
        total (int): total
        remark (str): remark
        enable (bool): enable
        expiry_time (int): expiry time
        listen (str): listen
        port (int): port
        protocol (str): protocol
        settings (str): settings
        stream_settings (str): stream settings
        tag (str): tag
        sniffing (str): sniffing

    Returns:
        Inbounds (Inbounds): Inbounds in database schema
    """
