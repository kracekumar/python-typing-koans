# -*- coding: utf-8 -

"""The code is copied from https://github.com/benoitc/gunicorn/blob/master/gunicorn/sock.py
A lot of code is removed here for sake of understanding.
"""
import errno
import logging
import os
import socket
import stat
import sys
import time
from dataclasses import dataclass
from typing import Optional, Type, TypeVar, Union

logger = logging.getLogger(__name__)


Address = Union[tuple[str, int], str, bytes]


@dataclass
class Config:
    address: Address
    reuse_port: bool
    umask: int
    uid: int = 1
    gid: int = 1
    backlog: int = 5


def is_ipv6(addr: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET6, addr)
    except socket.error:  # not a valid address
        return False
    except ValueError:  # ipv6 not supported on this platform
        return False
    return True


class BaseSocket:
    FAMILY = socket.AF_INET

    # Annotate log
    def __init__(self, address: Address, conf: Config, log):
        self.log = log
        self.conf = conf

        self.cfg_addr = address
        sock = socket.socket(self.FAMILY, socket.SOCK_STREAM)
        bound = False

        # annotate socket
        self.sock = sock

    def bind(self, sock) -> None:
        sock.bind(self.cfg_addr)

    def close(self) -> None:
        if self.sock is None:
            return

        try:
            self.sock.close()
        except socket.error as e:
            self.log.info("Error while closing socket %s", str(e))

        self.sock = None

    # Annotate
    def set_options(self, sock, bound: bool = False):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.conf.reuse_port and hasattr(socket, "SO_REUSEPORT"):  # pragma: no cover
            try:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except socket.error as err:
                if err.errno not in (errno.ENOPROTOOPT, errno.EINVAL):
                    raise
        if not bound:
            self.bind(sock)
        sock.setblocking(False)

        # make sure that the socket can be inherited
        if hasattr(sock, "set_inheritable"):
            sock.set_inheritable(True)

        sock.listen(self.conf.backlog)
        return sock


class TCPSocket(BaseSocket):

    FAMILY = socket.AF_INET

    def set_options(self, sock, bound: bool = False):
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        return super().set_options(sock, bound=bound)


class TCP6Socket(TCPSocket):

    FAMILY = socket.AF_INET6


class UnixSocket(BaseSocket):
    FAMILY = socket.AF_UNIX

    def __init__(self, addr: str, conf: Config, log):
        try:
            st = os.stat(addr)
        except OSError as e:
            log.error("Not unix socket", exc_info=True)
        super().__init__(addr, conf, log)

    def bind(self, sock) -> None:
        old_umask = os.umask(self.conf.umask)
        sock.bind(self.cfg_addr)
        # Chown address


# annotate return type without using Union
def _sock_type(addr: Address):
    if isinstance(addr, tuple):
        if is_ipv6(addr[0]):
            return TCP6Socket
        else:
            return TCPSocket
    elif isinstance(addr, (str, bytes)):
        return UnixSocket
    else:
        raise TypeError("Unable to create socket from: %r" % addr)


def create_sockets(conf: Config, log: logging.Logger):
    """
    Create a new socket for the configured addresses.

    If a configured address is a tuple then a TCP socket is created.
    If it is a string, a Unix socket is created. Otherwise, a TypeError is
    raised.
    """
    listeners = []

    # get it only once
    address: Address = conf.address
    sock_type = _sock_type(address)
    sock = None
    for i in range(5):
        try:
            sock = sock_type(address, conf, log)
        except socket.error as e:
            log.error("Failed to connect", exc_info=True)
            if i < 5:
                msg = "connection to {address} failed: {error}"
                log.debug(msg.format(addr=str(address), error=str(e)))
                log.error("Retrying in 1 second.")
                time.sleep(1)
        else:
            break

    if sock is None:
        log.error("Can't connect to %s", str(address))
        sys.exit(1)

    listeners.append(sock)

    return listeners


def main() -> None:
    listeners = create_sockets(
        Config(address=("127.0.0.1", 19999), reuse_port=False, umask=1), logger
    )


if __name__ == "__main__":
    main()
