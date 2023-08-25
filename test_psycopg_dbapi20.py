#!/usr/bin/env python

# Test suite driver for psycopg2. This is not official - more an example.

import dbapi20
import unittest
import psycopg2  # Bug #877952
import subprocess

class test_Psycopg(dbapi20.DatabaseAPI20Test):
    driver = psycopg2
    connect_kw_args = {
        'host': 'localhost',
        'user': 'root',
        'dbname': 'dbt',
        'password': 'password'
        }

    lower_func = 'lower' # For stored procedure test

    def setUp(self):
        # Call superclass setUp In case this does something in the
        # future
        dbapi20.DatabaseAPI20Test.setUp(self) 

        try:
            con = self._connect()
            con.close()
        except:
            cmd = [ "psql", "-c", "create database dbapi20_test" ]
            if subprocess.call(cmd):
                self.fail("Failed to create databse.")

    def tearDown(self):
        dbapi20.DatabaseAPI20Test.tearDown(self)

    def test_non_idempotent_close(self): pass
    def test_nextset(self): pass
    def test_setoutputsize(self): pass

if __name__ == '__main__':
    unittest.main()
