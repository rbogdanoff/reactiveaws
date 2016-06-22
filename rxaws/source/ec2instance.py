"""AWS Instance object source
   This class is a 'wrapper' for the boto instance list.
"""

from .sourcebase import SourceBase

class Ec2Instance(SourceBase):
    """Class that wraps a list of ec2 dict objects  """

    @staticmethod
    def get_state(ec2_dict):
        """
        Static helper method - returns the instance state (e.g. 'stopped', 'running') from an ec2
        dict

        :param ec2_dict: an 'ec2 dict' object.
        :return: a string that is the ec2 instance state ('stopped', 'running' ect.)
        """
        return ec2_dict['State']['Name']

    ## TODO: add more 'get helper' methods for commonly used attributes inside of ec2_dict

    def __init__(self, region_name=None):
        super().__init__(region_name)

    def get_source_iterable(self):
        """
        :return: an iterable of ec2 instance dict objects
        """
        return [ec2inst
                for reservation in self.conn.describe_instances()['Reservations']
                for ec2inst in reservation['Instances']]
