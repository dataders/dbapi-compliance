#!/usr/bin/env python

# Test suite driver for psycopg2. This is not official - more an example.

import os
import dbapi20
import databricks.sql
from test_psycopg_dbapi20 import TestPsycopg

class TestDatabricksConnector(dbapi20.DatabaseAPI20Test):
    # driver = psycopg2
    driver = databricks.sql
    connect_kw_args = {
        'server_hostname': os.environ.get('DBT_DATABRICKS_HOST_NAME'),
        'http_path':  os.environ.get('DBT_DATABRICKS_HTTP_PATH'),
        'token':  os.environ.get('DBT_DATABRICKS_TOKEN')
        }
