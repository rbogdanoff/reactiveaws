"""Abstract class for source objects.  Source objects are interables the contain
   aws service objects (e.g. ec2 instances or ebs volumes) that can be used
   as input into an rx Observable (a stream)
"""
from abc import abstractmethod, ABCMeta
import boto3

class SourceBase(metaclass=ABCMeta):
    """Abstract/base class for all concrete source classes"""
    default_region_name = 'us-east-1'

    def __init__(self, region_name=None, service='ec2'):
        """

        :param region_name: the aws region to connect to.  Defaults to us-east-1
        :param service: the aws service to connect to.  Defaults to ec2
        """

        self.region_name = SourceBase.default_region_name if region_name is None else region_name
        self.service = service
        self.conn = boto3.client(service, region_name=self.region_name)
        self.aws_iter = None

    def __iter__(self):
        """Returns itself as an iterable object"""
        self.aws_iter = iter(self.get_source_iterable())
        return self

    def __next__(self):
        """Returns next value of wrapped aws dict"""
        return next(self.aws_iter)

    @abstractmethod
    def get_source_iterable(self):
        """ concrete subclass implements this by providing aws (boto3) function
            that will return iterable of aws object type represented by the class
        """
        return NotImplemented
