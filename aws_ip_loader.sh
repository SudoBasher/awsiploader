#!/bin/bash

###########################################################
## AWS IP Loader
## https://github.com/sudobasher/awsiploader
###########################################################

## notes:
## use this to quickly add your ip to a couple aws security groups

## usage:
# ./aws_ip_loader.sh add
# ./aws_ip_loader.sh delete

## import global settings
. ./config.sh

## title
echo
echo "** AWS IP Loader **"
echo 

## california
echo "Modifying AWS California security group..."
cd $aws_env_dir
. $aws_ca_env
if [ $transaction_type == "add" ]
  then
    aws ec2 authorize-security-group-ingress --group-name $aws_ca_security_group --protocol tcp --port 22 --cidr $workstation_ip/32
fi
if [ $transaction_type == "delete" ]
  then
    aws ec2 revoke-security-group-ingress --group-name $aws_ca_security_group --protocol tcp --port 22 --cidr $workstation_ip/32
fi
echo

## beijing
echo "Modifying AWS Beijing security group..."
cd $aws_env_dir
. $aws_bj_env
if [ $transaction_type == "add" ]
  then
    aws ec2 authorize-security-group-ingress --group-name $aws_bj_security_group --protocol tcp --port 22 --cidr $workstation_ip/32
fi
if [ $transaction_type == "delete" ]
  then
    aws ec2 revoke-security-group-ingress --group-name $aws_bj_security_group --protocol tcp --port 22 --cidr $workstation_ip/32
fi
echo

## wrap up
echo "Completed".
echo
