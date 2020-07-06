import importlib
import os
import sys
from logging import getLogger

logger = getLogger(__name__)

def load_config():
    config_name = os.environ.get("TG_CONFIG")
    if config_name is None:
        config_name = "development"
    try:
        config = importlib.import_module("{}".format(config_name))
        print("Loaded config \"{}\" - OK".format(config_name))
        return config
    except (TypeError, ValueError, ImportError):
        print("Invalid config \"{}\"".format(config_name))
        sys.exit(1)