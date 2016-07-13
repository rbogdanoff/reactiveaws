"""AWS Region object source
   This class is a 'wrapper' for the boto region list. Wrapper is being
   used because we may want custom behavior in the future """

from .sourcebase import SourceBase

class RegionSource(SourceBase):
    """Class that wraps list of region dict objects """
    def __init__(self, region_name=None):
        super().__init__(region_name)

    def execute(self):
        """
        :return: list of aws region dict objects
        """
        def func(conn):
            return conn.describe_regions()['Regions']

        return super().execute(func)
