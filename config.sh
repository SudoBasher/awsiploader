#!/bin/bash

## user config:
aws_env_dir="/home/user/.aws"
aws_bj_env="aws-bj-env.sh"
aws_bj_security_group="security_group_1"
aws_ca_env="aws-ca-env.sh"
aws_ca_security_group="security_group_1"

## app config:
if [ $1 ]
  then
    transaction_type=$1
  else
    transaction_type="add"
fi
workstation_ip=$(eval 'dig +short myip.opendns.com @resolver1.opendns.com')
