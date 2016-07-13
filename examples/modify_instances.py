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
    add_tag_on_all_instances_in_one_region_in_batches()

def add_tag_on_all_instances_in_one_region():
    """
    will add a tag on all ec2 instances in a region
    :return:
    """
    print('add tag on all ec2 instances in us-east-1')

    # create task worker
    ec2_task = Ec2InstanceTask('us-east-1')

    # create stream of ec2 instance dict objects
    ec2_stream = Observable.from_(Ec2InstanceSource('us-east-1').execute())
    # for each ec2 instance, create a Tag
    ec2_stream.subscribe(on_next=lambda ec2_dict : ec2_task
                                                     .create_tags([ec2_dict],
                                                                  [{'Key':'reactaws_example',
                                                                    'Value':'some_value'}]))

def add_tag_on_all_instances_in_one_region_in_batches():
    """
    will add a tag on all ec2 instances in a region
    :return:
    """
    print('add tag on all ec2 instances in us-east-1 in batches')

    # create task worker
    ec2_task = Ec2InstanceTask('us-east-1')

    # create stream of ec2 instance dict objects
    ec2_stream = Observable.from_(Ec2InstanceSource('us-east-1').execute())
    ec2_stream \
        .buffer_with_count(20) \
        .subscribe(on_next=lambda ec2_dict_list:ec2_task.create_tags(ec2_dict_list,
                                                   [{'Key': 'reactaws_example',
                                                     'Value': 'some_value1'}]))


# TODO: add more examples ... add tags in batches, remove tags
if __name__ == '__main__':
    main()
