from rx import *
from rxaws.source.ec2instance import *
from rxaws.source.region import *
from rxaws.task.ec2instance import *

"""
Some simple examples for using rx to moodify AWS instances
"""
def main():
    """
    run all the examples!!
    """
    add_tag_on_all_instances_in_one_region()

def add_tag_on_all_instances_in_one_region():
    """
    will add a tag on all ec2 instances in a region
    :return:
    """
    print('add tag on all ec2 instances in us-east-1')

    # create task worker
    ec2_task = Ec2InstanceTask('us-east-1')

    # create stream of ec2 instance dict objects
    ec2_stream = Observable.from_iterable(Ec2InstanceSource('us-east-1'))
    # for each ec2 instance, create a Tag
    ec2_stream.subscribe(on_next=lambda ec2_dict : ec2_task.create_tags([ec2_dict],
                                                    [{'Key':'reactaws_example', 'Value':'some_value'}]))

# TODO: add more examples ... add tags in batches, remove tags