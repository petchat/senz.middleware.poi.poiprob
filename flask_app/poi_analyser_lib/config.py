__all__ = ["LOGENTRIES_TOKEN", "ROLLBAR_TOKEN", "APP_ENV"]
import os
from exception import *

# Settings

LOGENTRIES_DEV_TOKEN = "8c97ce63-1122-4f25-bd19-2dbdccd74262"
LOGENTRIES_PROD_TOKEN = "1ecd5d3b-50ef-4901-98e6-90913fccd247"
LOGENTRIES_LOCAL_TOKEN = "8c97ce63-1122-4f25-bd19-2dbdccd74262"

ROLLBAR_DEV_TOKEN = "5880ff452a72481fb3af605801652a63"
ROLLBAR_PROD_TOKEN = "5880ff452a72481fb3af605801652a63"
ROLLBAR_LOCAL_TOKEN = "5880ff452a72481fb3af605801652a63"

LOGENTRIES_TOKEN = ""
ROLLBAR_TOKEN = ""
APP_ENV = ""

# Configuration

try:
    APP_ENV = os.environ["APP_ENV"]
except KeyError, key:
    print "KeyError: There is no env var named %s" % key
    print "The local env will be applied"
    APP_ENV = "local"
finally:
    if APP_ENV == "dev":
        LOGENTRIES_TOKEN = LOGENTRIES_DEV_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_DEV_TOKEN
    elif APP_ENV == "prod":
        LOGENTRIES_TOKEN = LOGENTRIES_PROD_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_PROD_TOKEN
    elif APP_ENV == "local":
        LOGENTRIES_TOKEN = LOGENTRIES_LOCAL_TOKEN
        ROLLBAR_TOKEN = ROLLBAR_LOCAL_TOKEN
