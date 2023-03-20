from subprocess import Popen, PIPE
from json import dumps


class V2ray:
    def __init__(self, binary_path: str, config: dict):
        self._binary_path = binary_path
        self._config = config
        self._process = None

    def start(self):
        if self._process is not None:
            raise RuntimeError("V2ray is already running")

        with open('.c.json', 'wb') as cf:
            cf.write(dumps(self._config).encode())

        self._process = Popen(
            [self._binary_path, 'run', '-c', '.c.json'],
            stdin=PIPE,
            stdout=PIPE,
        )

        while output := self._process.stdout.readline().decode():
            print(output)
            if 'started' in output:
                break
