import os
from dotenv import load_dotenv

load_dotenv()

from .base import *

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .local import *
