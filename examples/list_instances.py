from rx import *
from rxaws.source.ec2instance import *
from rxaws.source.region import *

"""
Some simple examples for using rx with AWS object streams
"""
def main():
    """
    run all the examples!!
    """
    list_all_instances_in_one_region()
    list_all_instances_in_all_regions()
    list_instances_stopped()

def list_all_instances_in_one_region():
    """
    print the ec2 instances in one region
    :return:
    """
    print('list all ec2 instances in us-east-1')
    ec2_stream = Observable.from_iterable(Ec2Instance('us-east-1')) # create a stream of ec2 objects
    ec2_stream.subscribe(SimpleObserver())                          # SimpleObserver will print the ec2 instances

def list_all_instances_in_all_regions():
    """
    print all ec2 instances in all regions.
    1.  get a stream of all regions
    2.  for each region in the stream, get the ec2instance lists and flat_map them
    :return:
    """
    print('list all ec2 instances in all regions')
    region_stream = Observable.from_iterable(Region())              # create a stream of region objects
                                                                    # and get all ec2 instances in each region
    region_stream \
        .flat_map(lambda region : Ec2Instance(region['RegionName'])) \
        .subscribe(on_next=lambda x: print("Got: %s" % x))

def list_instances_stopped():
    """
    print all ec2 instances that are stopped.
    1.  get a stream ec2 instacnes
    2.  filter for only ec2 instance that are State -> Name is 'stopped'
    :return:
    """
    print('list all ec2 instances stopped us-east-1')
    ec2_stream = Observable.from_iterable(Ec2Instance('us-east-1')) # create a stream of ec2 objects
    ec2_stream.filter(lambda ec2 : ec2['State']['Name'] == 'stopped') \
        .subscribe(SimpleObserver())



class SimpleObserver(Observer):
    """
    A simple observer that will print events (objects) it received from a stream
    """
    def on_next(self, x):
        print("Got: %s" % x)

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("completed")

if __name__ == '__main__':
    main()