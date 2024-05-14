#!/usr/bin/env python

# Test suite driver for psycopg2. This is not official - more an example.

import os
import dbapi20
import redshift_connector


class TestRedshiftConnector(dbapi20.DatabaseAPI20Test):
    # driver = psycopg2
    driver = redshift_connector
    connect_kw_args = {
        "host": os.environ.get("REDSHIFT_TEST_HOST"),
        "user": os.environ.get("REDSHIFT_TEST_USER"),
        "database": os.environ.get("REDSHIFT_TEST_DBNAME"),
        "password": os.environ.get("REDSHIFT_TEST_PASS"),
    }
