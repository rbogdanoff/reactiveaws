from nose.tools import *
from unittest.mock import patch, Mock
from rxaws.task.taskbase import TaskBase
from botocore.client import BaseClient


class BaseClient(Mock):
    """ mock boto BaseClient, won't really do anything"""

class TestTaskBase:
    # inject the mock BaseClient
    @patch('boto3.client', return_value=(BaseClient()))
    def setup(self, mock_return_value):
        # create instance of class under test
        self.cut_taskbase = TaskBase()

    def teardown(self):
        pass

    def test_taskbase_create(self):
        # when a new TaskBase instance is created
        # is should contain an aws client
        assert self.cut_taskbase.conn is not None
        assert isinstance(self.cut_taskbase.conn, BaseClient) is True, \
            'expected BaseClient got: %s' % type(self.cut_taskbase.conn)
