"""Abstract class for source objects.  Source objects are interables the contain
   aws service objects (e.g. ec2 instances or ebs volumes) that can be used
   as input into an rx Observable (a stream)
"""
from abc import abstractmethod, ABCMeta
from boto import ec2

class SourceBase(metaclass=ABCMeta):
	"""Abstract/base class for all concrete source classes"""
	default_region_name = 'us-west-1'

	def __init__(self, region_name=None):
		"""concrete subclass to pass in the iterable to wrap"""
		region_name = SourceBase.default_region_name if region_name is None else region_name
		self.conn = ec2.connect_to_region(region_name)

	def __iter__(self):
		"""Returns itself as an iterable object"""
		self.aws_iter = iter(self.get_source_iterable())
		return self

	def __next__(self):
		"""Returns next value of wrapped aws object iter"""
		return next(self.aws_iter)

	@abstractmethod
	def get_source_iterable(self):
		return NotImplemented
        