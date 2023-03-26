import os

from .base import *

if os.environ.get('V2ENV', 'dev') == 'prod':
    from .prod import *
else:
    from .dev import *

from .jet import *
from .v2ray import *
from .telbot import *
from .faker import *