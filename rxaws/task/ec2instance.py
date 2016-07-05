"""
This class provides methods to do common AWS tasks
"""

from .taskbase import TaskBase

class Ec2InstanceTask(TaskBase):
    """Class that provides ec2 instances task execution  """


    def __init__(self, region_name=None):
        super().__init__(region_name, 'ec2')

    def create_tags(self, ec2_dict_list, tag_dict_list, dry_run=False):
        """
        will create tags on the ec2 instances in ec2_dict_list
        :param ec2_dict_list: a list of ec2_dict objects (as returned by rxaws.source.ec2instnace.Ec2instanceSource
        :param tag_dict_list: a list to tag dict objects.  a tag dict is { 'Key': 'key name', 'Value': 'value' }
        :param dry_run: if True, will not apply tags.  Default is False
        :return:
        """
        # create a list of instanceIds from ec2_dict_list
        def func(conn):
            instance_list = [inst_dict['InstanceId'] for inst_dict in ec2_dict_list ]
            self.conn.create_tags(
                DryRun=dry_run,
                Resources=instance_list,
                Tags=tag_dict_list
            )
        self.execute(func)

#TODO: add many more convenience task methods and a generic way to pass any boto3 ec2 update function