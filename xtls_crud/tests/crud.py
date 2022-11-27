import unittest
from uuid import uuid4
import random

import os

print(f"Setting up environment for {__name__}")
os.environ['DEBUG'] = 'True'
os.environ['ENVIRONMENT'] = 'dev'



def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))


try:
    from xtls_crud.xtls_crud.database import crud
    from xtls_crud.xtls_crud.database import schemas
    from xtls_crud.xtls_crud.utils.inbounds.builder import (
        InboundBuilder,
        SettingBuilder,
        StreamSettingBuilder,
        SniffingBuilder
    )
    from xtls_crud.xtls_crud.models.inbounds import (
        TlsSettings,
        Certificate,
        WsSettings,
        Client
    )
except ModuleNotFoundError:
    print('ModuleNotFoundError caught, adding parent directory to path')
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.parent.parent))
    from xtls_crud.xtls_crud.database import crud
    from xtls_crud.xtls_crud.database import schemas
    from xtls_crud.xtls_crud.utils.inbounds.builder import (
        InboundBuilder,
        SettingBuilder,
        StreamSettingBuilder,
        SniffingBuilder
    )
    from xtls_crud.xtls_crud.models.inbounds import (
        TlsSettings,
        Certificate,
        WsSettings,
        Client
    )


class Test(unittest.IsolatedAsyncioTestCase):
    async def test_get_multi(self):
        _ = await crud.inbounds.get_multi()
        print(_)

    async def deprecated_test_create_from_sample(self):  # noqa  # deprecated
        sample = schemas.InboundsCreate(
            user_id=1,
            up=random.randint(1, 100),
            down=random.randint(1, 100),
            total=random.randint(1, 100),
            remark=random_string(10),
            enable=True,
            expiry_time=random.randint(1, 100),
            listen=random_string(10),
            port=random.randint(1, 40000),
            protocol='vless',
            settings='test',
            stream_settings=random_string(10),
            tag=random_string(10),
            sniffing=random_string(10)
        )
        _ = await crud.inbounds.create(obj_in=sample)
        print(_)

    async def test_create_from_builder(self):
        setting_ = SettingBuilder(
        ).with_clients(
            [Client(id=uuid4(), alterId=0)]
        ).with_disable_insecure_encryption(
            False
        ).build()

        stream_setting_ = StreamSettingBuilder(
        ).with_network(
            "ws"
        ).with_security(
            "tls"
        ).with_tls_settings(
            TlsSettings(serverName="definitely-not-illegal.tech", certificates=[
                Certificate(certificateFile="/root/cert.crt", keyFile="/root/private.key")
            ])
        ).with_ws_settings(
            WsSettings(path="/sajsa2", headers={})
        ).build()

        sniffing_ = SniffingBuilder(
        ).with_enabled(
            True
        ).with_dest_override(
            ["http", "tls"]
        ).build()

        inbound = InboundBuilder(
        ).with_user_id(
            1
        ).with_up(
            '1GB'
        ).with_down(
            1
        ).with_total(
            1
        ).with_remark(
            'Nice'
        ).with_enable(
            False
        ).with_expiry_time(
            '1D'
        ).with_listen(
            ''
        ).with_port(
            random.randint(1, 40000)
        ).with_protocol(
            'vless'
        ).with_settings(
            setting_
        ).with_stream_settings(
            stream_setting_
        ).with_tag(
            random_string(10)
        ).with_sniffing(
            sniffing_
        ).build()

        _ = await crud.inbounds.create(obj_in=inbound)

        print(_)


if __name__ == '__main__':
    unittest.main()
