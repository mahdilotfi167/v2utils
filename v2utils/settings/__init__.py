import os

from .base import *

if os.environ.get('V2ENV', 'dev') == 'prod':
    from .prod import *
    IS_PROD = True
else:
    from .dev import *
    IS_PROD = False

from .jet import *
from .v2ray import *
from .telbot import *
from .faker import *