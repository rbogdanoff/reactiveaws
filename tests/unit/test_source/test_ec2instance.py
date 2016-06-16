from nose.tools import *
from unittest import mock
from rxaws.source import ec2instance
import boto.ec2.instance

class TestEc2Region:

	def setup(self):
		# create instance of class under test
		self.cut_ec2instance = ec2instance.Ec2Instance()

	def teardown(self):
		pass
	
	@nottest # FIXME: currently working on a better mock - perhaps next checking
	def test_source_type(self):
		# instance iterator should return elements of correct type
		# This mock was just a temp hack it is going away next checkin with a better one
		self.cut_ec2instance.get_source_iterable = mock.Mock(return_value=[boto.ec2.instance.Instance()])
		result = self.cut_ec2instance.get_source_iterable()[0]
		assert isinstance(result, boto.ec2.instance.Instance), \
							'expected boto.ec2.instance.Instance but got %s' % type(result)
