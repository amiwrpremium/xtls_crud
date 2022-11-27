import unittest

try:
    from xtls_crud.xtls_crud.models.inbounds import (
        TlsSettings,
        Certificate,
        WsSettings,
        Client
    )
    from xtls_crud.xtls_crud.utils.inbounds.builder import (
        InboundBuilder,
        SettingBuilder,
        StreamSettingBuilder,
        SniffingBuilder
    )
except ModuleNotFoundError:
    print('ModuleNotFoundError caught, adding parent directory to path')
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.parent.parent))

    from xtls_crud.xtls_crud.models.inbounds import (
        TlsSettings,
        Certificate,
        WsSettings,
        Client
    )
    from xtls_crud.xtls_crud.utils.inbounds.builder import (
        InboundBuilder,
        SettingBuilder,
        StreamSettingBuilder,
        SniffingBuilder
    )


class Test(unittest.TestCase):
    def test_setting_builder(self):
        setting_ = SettingBuilder(
        ).with_clients(
            [Client(id="438be03a-035f-44f4-a564-b30ff95442e3", alterId=0)]
        ).with_disable_insecure_encryption(
            False
        ).build()

        return setting_

    def test_stream_builder(self):
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

        return stream_setting_

    def test_sniffing_builder(self):
        sniffing_ = SniffingBuilder(
        ).with_enabled(
            True
        ).with_dest_override(
            ["http", "tls"]
        ).build()

        return sniffing_

    def test_inbound_builder(self):
        inbound = InboundBuilder(
        ).with_user_id(
            123
        ).with_up(
            1
        ).with_down(
            1
        ).with_total(
            1
        ).with_remark(
            'Nice'
        ).with_enable(
            False
        ).with_expiry_time(
            12313131
        ).with_listen(
            ''
        ).with_port(
            12
        ).with_protocol(
            'vless'
        ).with_settings(
            self.test_setting_builder()
        ).with_stream_settings(
            self.test_stream_builder()
        ).with_tag(
            'nice'
        ).with_sniffing(
            self.test_sniffing_builder()
        ).build()

        print(inbound.json())


if __name__ == '__main__':
    unittest.main()
