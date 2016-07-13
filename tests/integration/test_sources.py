"""these are live tests - you need to have the env vars AWS_ACCESS_KEY_ID and
   AWS_SECRET_ACCESS_KEY set and you will need to have (at this time) an EC2
   instance, running or stopped, in the us-east-1 region

   TODO:  setup a mock server (e.g. http://www.mbtest.org/ or http://www.mock-server.com/)
   as an alternative to live testing.
"""

from nose.tools import *
import os
import sys
import pickle
from rxaws.source.region import *
from rxaws.source.ec2instance import *

def test_region_source():
    # Region should return list of dict where dict has a key 'RegionName'
    test_source((RegionSource(), 'RegionName', sys._getframe().f_code.co_name))
    # put more tests here if needed

def test_ec2instance_source():
    # Ec2Instance should return list of dict where dict has a key 'InstanceId'
    test_source((Ec2InstanceSource(), 'InstanceId', sys._getframe().f_code.co_name))
    # put more tests here if needed

@nottest
def test_source(spec_tuple):
    """
    helper function to test concrete source classes
    :param spec_tuple: [0] class under test
                       [1] the key in the returned dict we expect
                       [2] this function's name
    :return:
    """
    # a source object should return a list of dict where the dict has
    # an expected key
    result = spec_tuple[0].execute()[0]
    assert spec_tuple[1] in result, 'key %s does not exist' % spec_tuple[1]
    # if this test passed, emit the test data we can use it for test fixtures!!
    emit_fixture(spec_tuple)

def emit_fixture(spec_tuple):
    # if the env var EMIT_FIXTURES is set, then we want to emit the test data
    # we can use it for mock injection in other tests!!!
    if not os.getenv('EMIT_FIXTURES'):
        return
    # emit all the element of the source object to the fixtures directory
    fixture_file_name = os.getcwd() + '/tests/fixtures/source/' + spec_tuple[2] + '.ser'
    pickle.dump([elem for elem in spec_tuple[0].execute()], open(fixture_file_name, "wb"))



