import os
import logging
from subprocess import Popen, PIPE
from json import dumps
from .client import Client

logger = logging.getLogger(__name__)


def is_uds_address(addr):
    return addr.startswith('/')


def is_abstract_uds_address(addr):
    return addr.startswith('@')


class V2ray:
    CONFIG_PATH = '.config.json'

    def __init__(self, binary_path: str, api_address, api_port):
        self._binary_path = binary_path
        self._process: Popen = None
        self._client = Client(api_address, api_port)
        self._current_config = dict()

    @staticmethod
    def _write_config(config, path):
        with open(path, 'wb') as cf:
            cf.write(dumps(config).encode())

    def refresh_config(self, config):
        if config != self._current_config:
            logger.warning('V2ray config changed, restarting...')
            if self._restart_process(config):
                self._current_config = config
                logger.warning('V2ray restarted')
            else:
                self._restart_process(self._current_config)
                logger.error(
                    'V2ray restart failed, try to recover from last config')
            self._client.reconnect()

    @staticmethod
    def __remove_unix_domain_sockets(config):
        for inbound in config.get('inbounds', []):
            if is_uds_address(inbound.get('listen', '0.0.0.0')):
                try:
                    os.remove(inbound.get['listen'])
                except OSError:
                    pass

    def _restart_process(self, config):
        self._write_config(config, self.CONFIG_PATH)
        if self._process:
            self._process.terminate()
        # Remove unix domain sockets to prevent from address already in use errors
        self.__remove_unix_domain_sockets(config)
        self._process = Popen(
            [self._binary_path, 'run', '-c', self.CONFIG_PATH],
            stdin=PIPE,
            stdout=PIPE,
        )
        while output := self._process.stdout.readline().decode().strip():
            logger.warning(output)
            if 'started' in output:
                return True
        return False

    def get_user_traffics(self, reset=True):
        try:
            return self._client.get_user_traffics(reset=reset)
        except RuntimeError as e:
            logger.warning(e)
            return []

    def start(self, config):
        self.refresh_config(config)
