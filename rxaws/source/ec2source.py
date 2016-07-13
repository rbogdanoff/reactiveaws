"""AWS Instance object source
   This is a base class for ec2
"""

from .sourcebase import SourceBase

class Ec2Source(SourceBase):
    """Class that wraps a list of ec2 dict objects  """

    def __init__(self, region_name=None):
        super().__init__(region_name, 'ec2')

    def get_source_iterable(self):
        """ concrete subclass implements this by providing aws (boto3) function
            that will return iterable of aws object type represented by the class
        """
        return NotImplemented