from django.test import TestCase
from .models import *


class VmessConfigTest(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.group = Group.objects.create(title='gold')
        self.group.users.add(
            User.objects.create(
                username='johndue',
                uuid='90e4903e-66a4-45f7-abda-fd5d5ed7f797',
            )
        )
        self.vmess = Vmess.objects.create(
            tag='vmess-behind-cdn',
            listen='0.0.0.0',
            port=35902,
            sniffing_enabled=True,
            sniffing_dest_override='http,tls',
            group=self.group,
        )

    def test_tcp(self):
        transport = Tcp.objects.create(
            inbound=self.vmess,
            header_type='http',
            header_request_path='/vmtcp',
        )
        config = {
            'tag': 'vmess-behind-cdn',
            'listen': '0.0.0.0',
            'protocol': 'vmess',
            'port': 35902,
            'settings': {
                'clients': [
                    {
                        'email': 'johndue@vmess-behind-cdn',
                        'id': '90e4903e-66a4-45f7-abda-fd5d5ed7f797',
                    },
                ],
            },
            'streamSettings': {
                'network': 'tcp',
                'security': 'none',
                'tcpSettings': {
                    'acceptProxyProtocol': False,
                    'header': {
                        'type': 'http',
                        'request': {
                            'path': [
                                '/vmtcp',
                            ],
                        },
                    },
                },
            },
            'sniffing': {
                'enabled': True,
                'destOverride': [
                    'http',
                    'tls',
                ],
            },
        }
        self.assertDictEqual(self.vmess.get_server_config(), config)
