
## aws cli credentials
aws_environments = {}
## the key names below (IE: 'ca') is what matches each aws_target item in config_general.py to each aws_environment item name below
aws_environments['ca'] = { 'AWS_ACCESS_KEY_ID':'blah',
                           'AWS_SECRET_ACCESS_KEY':'blah',
                           'AWS_DEFAULT_REGION':'us-west-1',
                        }
