from nose.tools import *
from unittest.mock import patch, Mock
from rxaws.source.sourcebase import SourceBase
from boto.ec2.connection import EC2Connection
import boto.ec2


class UnitTestableEC2Connection(EC2Connection):
	""" subclass EC2Conection that won't really do anything """
	def __init__(self):
		pass

class TestSourceBase:
	# inject the bogus UnitTestableEC2Connection 
	@patch('boto.ec2.connect_to_region', return_value=(UnitTestableEC2Connection()))
	# mock the get_source_iterable abstractmethod
	@patch.multiple(SourceBase, __abstractmethods__=set(), get_source_iterable=Mock(return_value=[1,2,3]))
	def setup(self, mock_connection):
		# create instance of class under test
		self.cut_sourcebase = SourceBase()

	def teardown(self):
		pass

	def test_sourcebase_create(self):
		# when a new SourceBase instance is created
		# is should contain an EC2Connection
		assert self.cut_sourcebase.conn is not None
		#isinstance(a, dict)
		assert isinstance(self.cut_sourcebase.conn, EC2Connection) is True, \
			'expected EC2Connection got: %s' % type(self.cut_sourcebase.conn)

	@patch.multiple(SourceBase, __abstractmethods__=set(), get_source_iterable=Mock(return_value=[1,2,3]))
	def test_iteration(self):
		# given that SourceBase has a 'wrapped' iterable
		test_exception = None
		# when we iterate through SourceBase
		try:
			for elem in self.cut_sourcebase:
				pass
		except Exception as e:
			test_exception = e
		# it should not have raised any exceptions
		assert test_exception is None, 'exception raised: %s' % type(test_exception)
