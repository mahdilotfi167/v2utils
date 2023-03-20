import grpc
from typing import Iterable


class Traffic:
    def __init__(self, up, down):
        self._up = up
        self._down = down


class UserTraffic(Traffic):
    pass


class InboundTraffic(Traffic):
    pass


class Client:
    def __init__(self, address, port):
        self._channel = grpc.insecure_channel("%s:%s" % (address, port))

    def get_all_traffics(self) -> Iterable[Traffic]:
        pass
