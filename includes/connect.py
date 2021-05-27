from abc import ABC, abstractmethod
from dataclasses import dataclass
from .base import BaseConnect, ConnectArgs


@dataclass
class ConnectArgs:

    host: str
    device_hostname: str
    port: int
    timeout: int
    max_recv_time: int


class Connect(BaseConnect, ABC):
    def __init__(self, connect_args: ConnectArgs = None) -> None:

        self.error: str = None
        self.connect_args = connect_args

    @abstractmethod
    def connect(self):
        pass
