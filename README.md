# AWS IP Loader

Use this to quickly add your IP to a couple of AWS security groups.

## Setup

Run these two commands:

* cp config_credentials.py config_credentials.local.py
* cp config_general.py config_general.local.py

Then configure these two file:

* config_credentials.local.py

```
aws_environments['ca'] = { 'AWS_ACCESS_KEY_ID':'blah',
                           'AWS_SECRET_ACCESS_KEY':'blah',
                           'AWS_DEFAULT_REGION':'us-west-1',
                        }
```

Add an aws_environment array item for each of the AWS data centers you need to work with. IE: California, N. Virginia, and Frankfurt. The key names (IE: ca, nv, fr) will be referenced in `config_general.local.py`. Enter your aws key ids, secret access keys, and region associated with each AWS data center.

* config_general.local.py

```
aws_targets = ( { 'Environment':'California Development',
                  'Configuration':'ca',
                  'Security Group':'sg-12345678',
                },
              )
```

Add an aws_target array item for each security group you need to add your current IP to. The `Configuration` value will be looked up in the aws_environments array in order to find the correct credentials.

Yep, you can have multiple aws_targets per AWS datacenter.

Setup is all done.

## Use it

To add your current IP to your security groups:

```python aws_ip_loader.py```
or
```python aws_ip_loader.py add```

To remove your current IP to your security groups:

```python aws_ip_loader.py delete```
