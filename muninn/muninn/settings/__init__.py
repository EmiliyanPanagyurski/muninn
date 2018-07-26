import os

if os.environ.get("MUNINN_SETTINGS_ENV") == "production":
    from .prod import *
elif os.environ.get("MUNINN_SETTINGS_ENV") == "development":
    from .dev import *
