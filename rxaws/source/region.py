"""AWS Region object source
   This class is a 'wrapper' for the boto region list. Wrapper is being
   used because we may want custom behavior in the future """

from .sourcebase import SourceBase
import boto.ec2


class Region(SourceBase): # pylint: disable=too-few-public-methods
    """Class that wraps a list of boto.regioninfo.RegionInfo objects """
    def __init__(self, region_name=None):
        super().__init__(region_name)

    def get_source_iterable(self):
        return boto.ec2.regions()
