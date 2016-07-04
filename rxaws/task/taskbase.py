"""Abstract class for task objects.  Task objects perform AWS update operations
   and are used as rx Subscribers
"""
from abc import abstractmethod, ABCMeta
import boto3

class TaskBase(metaclass=ABCMeta):
    """Abstract/base class for all concrete task classes"""
    default_region_name = 'us-east-1'

    def __init__(self, region_name=None, service='ec2'):
        """
        :param region_name: the aws region to connect to.  Defaults to us-east-1
        :param service: the aws service to connect to.  Defaults to ec2
        """
        self.region_name = TaskBase.default_region_name if region_name is None else region_name
        self.service = service
        self.conn = boto3.client(service, region_name=self.region_name)

