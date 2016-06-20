"""AWS Instance object source
   This class is a 'wrapper' for the boto instance list.
"""

from .sourcebase import SourceBase

class Ec2Instance(SourceBase):
    """Class that wraps a list of ec2 dict objects  """
    def __init__(self, region_name=None):
        super().__init__(region_name)

    def get_source_iterable(self):
        """
        :return: an iterable of ec2 instance dict objects
        """
        return [ec2inst
                for reservation in self.conn.describe_instances()['Reservations']
                for ec2inst in reservation['Instances']]
