#!/usr/bin/env python2

__version__     = "1.0.1"
__author__      = "Paolo Latella"
__email__       = "paolo.latella@xpeppers.com"

from boto import ec2

tagfilters = {'tag:Schedule': 'ONOFF'}
instance_list = []

connection = ec2.connect_to_region("eu-west-1")
reservations = connection.get_all_instances(filters=tagfilters)
for r in reservations:
	for i in r.instances:
		instance_list.append(i.id)
connection.stop_instances(instance_ids=instance_list)