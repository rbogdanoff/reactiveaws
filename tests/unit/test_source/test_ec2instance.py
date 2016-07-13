from nose.tools import *
from unittest import mock
from rxaws.source.ec2instance import Ec2InstanceSource
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
        self.cut_ec2instance = Ec2InstanceSource()

    def teardown(self):
        pass

    @mock.patch.object(Ec2InstanceSource, 'execute', return_value=fixture)
    def test_source_type(self, mock_ec2):
        # instance iterator should return list
        result = self.cut_ec2instance.execute()
        assert isinstance(result, list), \
        					'expected list but got %s' % type(result)
        # of dict elements
        elem = result[0]
        assert isinstance(result[0], dict), 'expected dict but got %s' % type(result)
        # that has expected key
        assert 'InstanceId' in elem, 'key InstanceId does not exist'


    # test static helper methods
    def test_get_state(self):
        # setup - what is the ec2 state in the first ec2 dict in the test fixture?
        test_state = TestEc2Instance.fixture[0]['State']['Name']
        # when get_state helper method is called with an ec2 dict
        result = Ec2InstanceSource.get_state(TestEc2Instance.fixture[0])
        # it should return the ec2 instance state
        assert result == test_state, 'expected %s but got %s' % (test_state, result)

    def test_get_tags(self):
        # setup - what are the ec2 tags in the first ec2 dict in the test fixture
        test_tags = TestEc2Instance.fixture[0]['Tags']
        # when get_tags helper method is called with an ec2 dict
        result = Ec2InstanceSource.get_tags(TestEc2Instance.fixture[0])
        # it should return the ec2 instance tags
        assert result == test_tags, 'expected %s but got %s' % (test_tags, result)
