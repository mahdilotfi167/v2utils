from typing import Iterable
from base64 import b64encode


def links_to_sub(links: Iterable[str]):
    return b64encode('\n'.join(links).encode()).decode()
