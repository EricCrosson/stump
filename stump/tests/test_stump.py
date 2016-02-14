#!/usr/bin/env python
# Written by Eric Crosson
# 2016-02-14

import unittest
import stump

import os
import sys
import logging


@stump.ret('got {b}')
def ret(b):
    return b+1


@stump.pre('got {b}')
def pre(b):
    return b+1


@stump.post('got {b}')
def post(b):
    return b+1


@stump.put('got {b}')
def put(b):
    return b+1


class TestStump(unittest.TestCase):


    def delete_logfile(self):
        with open('test_output.log', 'w'):
            pass


    def setUp(self):
        self.delete_logfile()
        logging.basicConfig(filename='test_output.log', level=logging.DEBUG)
        logger = logging.getLogger()
        stump.configure(logger)


    def tearDown(self):
        pass


    def contents_of_logfile(self):
        with open('test_output.log') as f:
            return f.read()


    def test_ret(self):
        ret(5)
        self.assertEqual(self.contents_of_logfile(),
                         "INFO:root:ret:got 5...\nINFO:root:ret:got 5...done (returning 6)\n")


    def test_put(self):
        put(5)
        self.assertEqual(self.contents_of_logfile(),
                         "INFO:root:put:got 5...\nINFO:root:put:got 5...done\n")


    def test_pre(self):
        pre(5)
        self.assertEqual(self.contents_of_logfile(),
                         "INFO:root:pre:got 5...\n")


    def test_post(self):
        post(5)
        self.assertEqual(self.contents_of_logfile(),
                         "INFO:root:post:got 5...done\n")


    def test_log_level(self):
        pass


if __name__ == '__main__':
    sys.exit(unittest.main())
