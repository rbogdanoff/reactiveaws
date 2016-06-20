from nose.tools import *
from unittest import mock
from rxaws.source.ec2instance import Ec2Instance
from tests.unit.test_source.test_sourcebase import BaseClient
import os
import pickle

class TestEc2Instance:
    fixture_file_name = os.getcwd() + '/tests/fixtures/source/test_ec2instance_source.ser'
    fixture = pickle.load(open(fixture_file_name, "rb"))

    # need to mock the boto3 client
    @mock.patch('boto3.client', return_value=(BaseClient()))
    def setup(self, mock_client):
        # create instance of class under test
        self.cut_ec2instance = Ec2Instance()

    def teardown(self):
        pass

    @mock.patch.object(Ec2Instance, 'get_source_iterable', return_value=fixture)
    def test_source_type(self, mock_ec2):
        # instance iterator should return list
        result = self.cut_ec2instance.get_source_iterable()
        assert isinstance(result, list), \
        					'expected list but got %s' % type(result)
        # of dict elements
        elem = result[0]
        assert isinstance(result[0], dict), 'expected dict but got %s' % type(result)
        # that has expected key
        assert 'InstanceId' in elem, 'key InstanceId does not exist'
