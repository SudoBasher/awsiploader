
## imports
import subprocess
import sys
import os

## load config
execfile("functions.py")
execfile("config_general.local.py")
execfile("config_credentials.local.py")

## display title
display_title()

## configure display config
aws_transaction_type = configure_aws_transaction_type(selected_transaction_type)

## debug aws_targets
# display_targets(aws_targets)

## modify security groups
modify_aws_security_groups(aws_transaction_type, aws_targets, ip_address)
