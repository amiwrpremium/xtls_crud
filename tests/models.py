import unittest
import os

print(f"Setting up environment for {__name__}")
os.environ['DEBUG'] = 'True'
os.environ['ENVIRONMENT'] = 'dev'


try:
    from xtls_crud.xtls_crud.models.inbounds import (
        Setting,
        Sniffing,
        StreamSettings
    )
except ModuleNotFoundError:
    print('ModuleNotFoundError caught, adding parent directory to path')
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.parent.parent))

    from xtls_crud.xtls_crud.models.inbounds import (
        Setting,
        Sniffing,
        StreamSettings
    )


class Test(unittest.TestCase):
    def test_settings_model(self):
        _sample = {
            "clients": [
                {
                    "id": "438be03a-035f-44f4-a564-b30ff95442e3",
                    "alterId": 0
                }
            ],
            "disableInsecureEncryption": False
        }

        setting_ = Setting(**_sample)
        print(setting_.json())
        return setting_

    def test_sniffing_model(self):
        _sample = {
            "enabled": True,
            "destOverride": [
                "http",
                "tls"
            ]
        }

        sniffing_ = Sniffing(**_sample)
        print(sniffing_.json())
        return sniffing_

    def test_stream_settings_model(self):
        _sample = {
            "network": "ws",
            "security": "tls",
            "tlsSettings": {
                "serverName": "definitely-not-illegal.tech",
                "certificates": [
                    {
                        "certificateFile": "/root/cert.crt",
                        "keyFile": "/root/private.key"
                    }
                ]
            },
            "wsSettings": {
                "path": "/sajsa2",
                "headers": {}
            }
        }

        stream_settings_ = StreamSettings(**_sample)
        print(stream_settings_.json())
        return stream_settings_


if __name__ == '__main__':
    unittest.main()
