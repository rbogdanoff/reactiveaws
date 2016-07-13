from nose.tools import *
from unittest import mock
from rxaws.source.region import RegionSource
from rxaws.source.sourcebase import SourceBase
from tests.unit.test_source.test_sourcebase import BaseClient
import pickle
import os


class TestRegion:
    fixture_file_name = os.getcwd() + '/tests/fixtures/source/test_region_source.ser'
    fixture = pickle.load(open(fixture_file_name, "rb"))

    # need to mock the boto3 client
    @mock.patch('boto3.client', return_value=(BaseClient()))
    def setup(self,  mock_client):
        # create instance of class under test
        self.cut_region = RegionSource()

    def teardown(self):
        pass

    @mock.patch.object(RegionSource, 'execute', return_value=fixture)
    def test_source_type(self, mock_region):
        # instance iterator should return list
        result = self.cut_region.execute()
        assert isinstance(result, list), \
                          'expected list but got %s' % type(result)
        # that contains dict elements
        elem = result[0]
        assert isinstance(result[0], dict), 'expected dict but got %s' % type(result)
        # that has expected key
        assert 'RegionName' in elem, 'key RegionName does not exist'
