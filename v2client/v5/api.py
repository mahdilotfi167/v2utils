from subprocess import Popen, PIPE
from json import dumps
from .client import Client


class V2ray:
    CONFIG_PATH = '.config.json'

    def __init__(self, binary_path: str, api_address, api_port):
        self._binary_path = binary_path
        self._process: Popen = None
        self._client = Client(api_address, api_port)
        self.needs_restart = False
        self._current_config: str = ''

    @staticmethod
    def _write_config(config):
        with open(V2ray.CONFIG_PATH, 'wb') as cf:
            cf.write(dumps(config).encode())

    def refresh_config(self, config):
        if config != self._current_config:
            self._current_config = config
            self._write_config(config)
            self._restart_process()

    def _restart_process(self):
        if self._process:
            self._process.terminate()
        self._process = Popen(
            [self._binary_path, 'run', '-c', V2ray.CONFIG_PATH],
            stdin=PIPE,
            stdout=PIPE,
        )

    def get_user_traffics(self, reset=True):
        return self._client.get_user_traffics(reset=reset)

    def get_inbound_traffics(self, reset=True):
        return self._client.get_inbound_traffics(reset=reset)

    def get_all_traffics(self, reset):
        return self._client.get_all_traffics(reset=reset)

    def start(self, config):
        self.refresh_config(config)

        while output := self._process.stdout.readline().decode():
            print(output)
            if 'started' in output:
                break
