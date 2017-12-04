
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
aws_ports = ( '22',
            )

## dynamic config
ip_address = get_local_ip_address()

## runtime config
if ( len(sys.argv) > 1 ):
  if ( sys.argv[1] == 'delete' ):
    selected_transaction_type='delete'
  else:
    selected_transaction_type='add'
else:
  selected_transaction_type='add'
if ( len(sys.argv) > 2 ):
  if ( sys.argv[2] == 'all' ):
    selected_transaction_option='all'
  else:
    selected_transaction_option='single'
else:
  selected_transaction_option='single'

