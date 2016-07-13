from nose.tools import *
from unittest.mock import patch, Mock
from rxaws.source.sourcebase import SourceBase
from botocore.client import BaseClient


class BaseClient(Mock):
    """ mock boto BaseClient, won't really do anything"""

class TestSourceBase:
    # inject the mock BaseClient
    @patch('boto3.client', return_value=(BaseClient()))
    # mock the get_source_iterable abstractmethod
   # @patch.multiple(SourceBase, __abstractmethods__=set(), execute=Mock(return_value=[1,2,3]))
    def setup(self, mock_return_value):
        # create instance of class under test
        self.cut_sourcebase = SourceBase()

    def teardown(self):
        pass

    def test_sourcebase_create(self):
        # when a new SourceBase instance is created
        # is should contain an aws client
        assert self.cut_sourcebase.conn is not None
        assert isinstance(self.cut_sourcebase.conn, BaseClient) is True, \
            'expected BaseClient got: %s' % type(self.cut_sourcebase.conn)
