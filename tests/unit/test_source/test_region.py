from nose.tools import *
from unittest import mock
from rxaws.source.region import Region
import boto.ec2.regioninfo as ec2
import boto.regioninfo

class TestRegion:

	@mock.patch('boto.ec2.regions', return_value=[ ec2.EC2RegionInfo(name='us-west-2')])
	def setup(self, mock_return_value):
		self.mock_return_value = mock_return_value
		# create instance of class under test
		self.cut_region = Region()

	def teardown(self):
		pass
	
	def test_source_type(self):
		# instance iterator should return elements of correct type
		result = self.cut_region.get_source_iterable()[0]
		assert isinstance(result, boto.regioninfo.RegionInfo), \
							'expected boto.regioninfo.RegionInfo but got %s' % type(result)
