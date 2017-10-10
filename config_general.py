
## user config
aws_transaction_type = ''
aws_targets = ( { 'Environment':'California Development',
                  'Configuration':'ca',
                  'Security Group':'sg-12345678',
                },
                { 'Environment':'California Production',
                  'Configuration':'ca',
                  'Security Group':'sg-90abcdef',
                },
              )

## dynamic config
ip_address = get_ip()

## runtime config
if ( len(sys.argv) > 1 ):
  if ( sys.argv[1] == 'delete' ):
    selected_transaction_type='delete'
  else:
    selected_transaction_type='add'
else:
  selected_transaction_type='add'
