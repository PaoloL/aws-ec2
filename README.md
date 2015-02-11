# aws-ec2

Demo and utilities about AWS EC2 Services

## Scheduler OnOff

The file scheduler-onoff.py is a simple python script that start/stop instances about a tag
You can configure the stop instances or start instances modifyng the last row with
- Start: connection.start_instances(instance_ids=instance_list)
- Stop: connection.stop_instances(instance_ids=instance_list)

Furthermore use crontab (Linux) or taskmanager (windows) for execute the start or stop of instances at scheduled time

