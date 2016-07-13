"""AWS Instance object source
   This class is a 'wrapper' for the boto instance list.
"""

from .ec2source import Ec2Source

class Ec2InstanceSource(Ec2Source):
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

    @staticmethod
    def get_tags(ec2_dict):
        """
        Static helper method - returns the instance tags from an ec2
        dict

        :param ec2_dict: an 'ec2 dict' object.
        :return: a list for tag dicts
        """
        return ec2_dict['Tags']

    ## TODO: add more 'get' helper methods for commonly used attributes inside of ec2 dict

    def __init__(self, region_name=None):
        super().__init__(region_name)

    def execute(self):
        """
        :return: a list of ec2 instance dict objects
        """
        def func(conn):
           return [ec2inst
                for reservation in conn.describe_instances()['Reservations']
                for ec2inst in reservation['Instances']]

        return super().execute(func)
