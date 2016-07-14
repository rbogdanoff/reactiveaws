[![Build Status](https://travis-ci.org/rbogdanoff/reactiveaws.svg?branch=develop)](https://travis-ci.org/rbogdanoff/reactiveaws)
[![Coveralls Coverage Status](https://img.shields.io/coveralls/rbogdanoff/reactiveaws/develop.svg)]()

# reactiveaws
An AWS interface/toolkit based on ReactiveX
===========================================

This project is in a 'building up' phase!!

The goal of this project is to create a toolkit lib that will provide an interface to the
AWS API using Python ReactiveX http://reactivex.io/ https://github.com/ReactiveX/RxPY

The initial idea is provide some 'out of the box' multi-step AWS utilities that uses reactive style programming.
The 'components' used to build the 'out of the box' multi-step utils could be reused to create other AWS utilities.
The eventual direction is to provide a YAML based 'custom AWS utility' builder by which a user could create
custom AWS multi-step utilities via a YAML DSL.

A secondary goal is to learn ReactiveX 

If you have any thought, let me know!! ron.bogdanoff@gmail.com

Setup
=====
The project uses python3.5.  I strongly recommend you use a virtualenv.

After you create a virtualenv for this project, just cd to the project home directly and run...

`pip install -r requirements.txt`


Tests
=====
Currently there are unit and integration tests.

##Unit tests
Unit tests do not need any external resource e.g. they do not need to connect to any AWS account to work.  They have test fixtures which are in tests/fixtures.  Currently the test fixtures are serialized objects (pickles) that were created from live tests.  That is, there is a feature of the integration tests where it is possible to persist the returned AWS boto3 objects so they can be used as test fixtures in unittests.  More on this in a bit.

To run the unit tests do..
```bash
python setup.py unittest
```

##Integration tests
Integration tests need to access an AWS account.  Currently they are read only, that is, they are only doing boto3 describe methods.  For example, boto3 ec3 'describe_instances'.  However, I have hand setup some ec2 instances in my AWS account for integration tests to work.  At this time there is no classic 'setup'/'teardown' which would, for example, create a few ec2 instances, run the integration tests, then delete them.

So, for now I do not recommend running the integration tests, but if you do, you need to set ENV varables for your AWS account.  Since boto3 is used, all you need to do is create these two ENV vars...

```bash
AWS_SECRET_ACCESS_KEY=mySecretKey
AWS_ACCESS_KEY_ID=myAccessKey
```

Then you should be able to run the integration tests...
```bash
nosetests tests.integration
```

##Examples
There are a few examples of how to use rxpy with source and task 
objects.  See the examples directory

TDOD: create a simple script to run the examples.  For now you need to something like...
```bash
$ export PYTHONPATH=.
$ python examples/list_instances.py
```
Just make sure you have your AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID envs set and you are good to go

TODO: a readme with details about the examples --- coming soon

##Other notes.
* will soon create a command package that will have some common commands that will be useful.  Example: a 'backupebs' command.  The commands will be configurable via a yml file and then can simply be called from the command line.
* side project...testing.  Integration testing can be challanging as it is expensive (time and $$) to always use AWS live.  So, while something like a mockserver (http://www.mbtest.org/ for example) is useful, to have some sort of toolkit to easily create mock AWS responses quicky with little effort would be great.  Thinking about starting another project that would focus on this challange


