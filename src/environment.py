from datetime import datetime
import os
import logging

### @package environment
#
# Interacitons with the environment variables.
#

def load_env(key: str, default: str) -> str:
    """!
    os.getenv() wrapper that handles the case of None-types for not-set env-variables\n

    @param key: name of env variable to load
    @param default: default value if variable couldn't be loaded
    @return value of env variable or default value
    """
    value = os.getenv(key)
    if value:
        return value
    logger.warning(f"Can't load env-variable for: '{key}' - falling back to DEFAULT {key}='{default}'")
    return default


logger = logging.getLogger('my-bot')

TOKEN = os.getenv("TOKEN")  # reading in the token from config.py file

# loading optional env variables
PREFIX = load_env("PREFIX", "b!")
VERSION = load_env("VERSION", "unknown")  # version of the bot
OWNER_NAME = load_env("OWNER_NAME", "unknown")   # owner name with tag e.g. pi#3141
OWNER_ID = int(load_env("OWNER_ID", "100000000000000000"))  # discord id of the owner

# roles to give on verification
_ROLES = os.getenv('ROLES', "760434164146634752 880220270210740235")
GUILD = int(load_env("GUILD", "760421261649248296"))  # guild the bot is configured for
START_CHANNEL = int(load_env("START_CHANNEL", "877208002762002465"))  # channel to point members to after verification
# date after which members need to be joined so that the bot will capture their not pending but role-less existence
_NOT_BEFORE = load_env("NOT_BEFORE", "25.08.2021")
NOT_BEFORE = datetime.strptime(_NOT_BEFORE, "%d.%m.%Y")

CHECK_PERIOD = int(load_env("CHECK_PERIOD", "5"))

# rough sanity check if roles were given
if not _ROLES:
    error = "Can't load env-variable ROLES - Bot needs at least one role-id to start!\n"
    logger.error(error)
    raise KeyError(error)

ROLES = [int(role.strip()) for role in _ROLES.split(' ')]
