from nose.tools import *
from unittest import mock
from rxaws.task.ec2instance import Ec2InstanceTask
from rxaws.task import ec2instance
from tests.unit.test_task.test_taskbase import BaseClient
import os
import pickle

class TestEc2Instance:
    fixture_file_name = os.getcwd() + '/tests/fixtures/source/test_ec2instance_source.ser'
    fixture = pickle.load(open(fixture_file_name, "rb"))

    # need to mock the boto3 client
    @mock.patch('boto3.client')
    def setup(self, mock_client):
        # create instance of class under test
        self.cut_ec2instance = Ec2InstanceTask()

    def teardown(self):
        pass

    def test_create_tags(self):
        # when the create_tags method is called
        instance_list = [{'InstanceId' : '123'}]
        tag_list = [{ 'Key' : 'thekey', 'Value' : 'theval'}]
        self.cut_ec2instance.create_tags(instance_list, tag_list )
        # is should have called boto3 create_tags with expected parameters
        self.cut_ec2instance.conn.create_tags\
            .assert_called_with(DryRun=False, Resources=['123'], Tags=[{'Value': 'theval', 'Key': 'thekey'}])


