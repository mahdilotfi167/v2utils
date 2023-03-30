import grpc
from typing import Iterable
from .proto.app.stats.command import command_pb2_grpc as stats_command_pb2_grpc
from .proto.app.stats.command import command_pb2 as stats_command_pb2


class Traffic:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def __repr__(self):
        return self.__str__()


class InboundTraffic(Traffic):
    def __init__(self, tag, up, down):
        self.tag = tag
        super().__init__(up, down)

    def __str__(self):
        return f"{self.tag} {self.up}\u2191 {self.down}\u2193"


class UserTraffic(Traffic):
    def __init__(self, email, up, down):
        self.email = email
        super().__init__(up, down)

    def __str__(self):
        return f"{self.email} {self.up}\u2191 {self.down}\u2193"


class Client:
    def __init__(self, address, port):
        self._dest = "%s:%s" % (address, port)
        self._channel = grpc.insecure_channel(self._dest)
        
    def reconnect(self):
        self._channel = grpc.insecure_channel(self._dest)

    def _get_traffics(self, name, reset) -> Iterable[Traffic]:
        stub = stats_command_pb2_grpc.StatsServiceStub(self._channel)
        try:
            res = stub.QueryStats(stats_command_pb2.GetStatsRequest(
                name=name,
                reset=reset
            ))
            return res.stat
        except grpc.RpcError as e:
            raise RuntimeError('Could not connect to v2ray api') from e

    @staticmethod
    def __parse_stat(stat):
        the_type, the_id, _, link_type = stat.split('>>>')
        link = link_type.removesuffix('link')
        return the_type, the_id, link

    def get_user_traffics(self, reset=True) -> Iterable[UserTraffic]:
        traffics_by_email = dict()
        for stat in self._get_traffics(name='user', reset=reset):
            _, email, link = self.__parse_stat(stat.name)
            if email not in traffics_by_email:
                traffics_by_email[email] = UserTraffic(email, 0, 0)
            traffic = traffics_by_email.get(email)
            setattr(traffic, link, stat.value)
        return list(traffics_by_email.values())
