"""
This is a base class for ec2 tasks
"""

from .taskbase import TaskBase

class Ec2Task(TaskBase):
    """Class that provides ec2 task execution  """


    def __init__(self, region_name=None):
        super().__init__(region_name, 'ec2')
