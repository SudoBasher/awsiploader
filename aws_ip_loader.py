
## imports
import subprocess
import sys
import os

## load config
execfile("functions.py")
execfile("config_general_local.py")
execfile("config_credentials_local.py")

## display title
display_title()

## display config
aws_transaction_type = display_config(selected_transaction_type)

## debug aws_targets
# display_targets(aws_targets)

## modify security groups
modify_security_groups(aws_transaction_type, aws_targets, ip_address)
