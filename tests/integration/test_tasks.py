"""these are live tests - you need to have the env vars AWS_ACCESS_KEY_ID and
   AWS_SECRET_ACCESS_KEY set and you will need to have (at this time) an EC2
   instance, running or stopped, in the us-east-1 region

   TODO:  setup a mock server (e.g. http://www.mbtest.org/ or http://www.mock-server.com/)
   as an alternative to live testing.
"""

from nose.tools import *
import os
import sys
import time
import pickle
from rxaws.source.region import *
from rxaws.source.ec2instance import *
from rxaws.task.ec2instance import *

def test_create_ec2_tags():
    # setup - get live ec2_dict
    ec2_dict_list = [ inst for inst in Ec2InstanceSource() ]
    # setup - create tags we will create
    timestamp = str(time.time())
    tag_dict_list = [{'Key' : 'reactawstest', 'Value' : timestamp }]

    # exec test
    Ec2InstanceTask().create_tags(ec2_dict_list, tag_dict_list)

    # verify
    # just check first one
    assert (tag_dict_list[0] in next(iter(Ec2InstanceSource()))['Tags']) is True, \
        'The ec2 tags did not get created as expected'




