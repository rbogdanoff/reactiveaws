"""AWS Instance object source
   This class is a 'wrapper' for the boto instance list.
"""

from .sourcebase import SourceBase
import boto.ec2

class Ec2Instance(SourceBase): # pylint: disable=too-few-public-methods
	"""Class that wraps a list of boto ec2 instance objects """

	def __init__(self, region_name=None):
		super().__init__(region_name)

	def get_source_iterable(self):
		""" flatten ec2instances in each reservation """
		return [ec2inst for reservation in self.conn.get_all_reservations() for ec2inst in reservation.instances]
