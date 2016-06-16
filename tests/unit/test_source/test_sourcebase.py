from nose.tools import *
from unittest.mock import patch, Mock
from rxaws.source.sourcebase import SourceBase
from boto.ec2.connection import EC2Connection

class TestSourceBase:
	""" testing methods of an abstractclass.  Need to mock the @abstractmethods in this class """
	@patch.multiple(SourceBase, __abstractmethods__=set(), get_source_iterable=Mock(return_value=[1,2,3]))
	def setup(self):
		# create instance of class under test
		self.cut_sourcebase = SourceBase()

	def teardown(self):
		pass

	def test_sourcebase_create(self):
		# when a new SourceBase instance is created
		# is should contain an EC2Connection
		assert self.cut_sourcebase.conn is not None
		assert type(self.cut_sourcebase.conn) is EC2Connection

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
