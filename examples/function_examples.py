from rx import *
from rxaws.source.ec2instance import *
from rxaws.source.region import *
from rxaws.source.ec2source import *

"""
The classes in source and task are convenience classes.  For exaple. reactaws.source.ec2instance will
return a list of ec2 instances so by doing Ec2InstanceSource().execute() you are good to go to feed
into an Observable.  Many more conveniecne classes will be added.

If the convenience class does not (yet) exist, you can also execute any boto3 method directly

"""
def main():
    """
    run all the examples!!
    """
    list_all_ebs_volumes()

def list_all_ebs_volumes():
    """
    There is currently not an rxaws.source.ec2Ebs convenience class.  Here is how you can execute
    describe_volumes on your own
    :return:
    """
    print('list all ebs volumes')

    # create instance of the ec2 source worker
    ec2Source = Ec2Source('us-east-1')
    # use a lambda to pass to the ec2source execute method
    ec2_stream = Observable.from_(ec2Source.execute(lambda conn : conn.describe_volumes()['Volumes']))
    ec2_stream.subscribe(SimpleObserver())                          # SimpleObserver will print the volumes

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
