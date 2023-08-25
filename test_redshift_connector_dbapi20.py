#!/usr/bin/env python

# Test suite driver for psycopg2. This is not official - more an example.

import dbapi20
import pg8000.dbapi
import subprocess
from test_psycopg_dbapi20 import TestPsycopg

class TestPg8000(TestPsycopg):
    # driver = psycopg2
    driver = pg8000.dbapi
    connect_kw_args = {
        'host': 'localhost',
        'user': 'root',
        'database': 'dbt',
        'password': 'password'
        }

    lower_func = 'lower' # For stored procedure test

    def test_non_idempotent_close(self): pass
    def test_nextset(self): pass
    def test_setoutputsize(self): pass