
def configure_aws_transaction_type(selected_transaction_type):
  if ( selected_transaction_type == 'delete' ):
    print 'Transaction selected: Deleting IP'
    aws_transaction_type = 'revoke-security-group-ingress'
  else:
    print 'Transaction selected: Adding IP'
    aws_transaction_type = 'authorize-security-group-ingress'
  print 'Current IP Address: '+ip_address
  print
  return aws_transaction_type

def display_targets(aws_targets):
  for target in aws_targets:
    for attribute in target:
      print attribute+': '+target[attribute]
    print

def display_title():
  print
  print '** AWS IP Loader **'
  print

def get_local_ip_address():
  exec_get_ip_address = subprocess.Popen(["dig","+short","myip.opendns.com","@resolver1.opendns.com"], stdout=subprocess.PIPE)
  ip_address = exec_get_ip_address.stdout.read()
  ip_address = ip_address.rstrip()
  return ip_address

def modify_aws_security_groups(aws_transaction_type, aws_targets, ip_address):
  for target in aws_targets:
    for attribute in target:
      if ( attribute == 'Configuration' ):
        print 'Processing target: '+target['Environment']
        if target[attribute] in aws_environments:
          ## debug aws credentials
          # print aws_environments[target[attribute]]
          ## load aws credentials into environment
          os.environ['AWS_ACCESS_KEY_ID'] = aws_environments[target[attribute]]['AWS_ACCESS_KEY_ID']
          os.environ['AWS_SECRET_ACCESS_KEY'] = aws_environments[target[attribute]]['AWS_SECRET_ACCESS_KEY']
          os.environ['AWS_DEFAULT_REGION'] = aws_environments[target[attribute]]['AWS_DEFAULT_REGION']
          ## debug the environment's aws region
          # subprocess.call('echo $AWS_DEFAULT_REGION', shell=True)
    ## debug aws ec2 command
    # print 'aws ec2 '+aws_transaction_type+' --group-id '+target['Security Group']+' --protocol tcp --port 22 --cidr '+ip_address+'/32'
    if ( selected_transaction_option == 'single' ):
      for port in aws_ports:
        print '- Port: '+port
        subprocess.call('aws ec2 '+aws_transaction_type+' \
                          --group-id '+target['Security Group']+' \
                          --protocol tcp \
                          --port '+port+' \
                          --cidr '+ip_address+'\/32', shell=True)
    # elif ( selected_transaction_option == 'all' ):
    #   print '- All ports'
    #   subprocess.call('aws ec2 '+aws_transaction_type+' \
    #                     --group-id '+target['Security Group']+' \
    #                     --protocol tcp \
    #                     --cidr '+ip_address+'\/32', shell=True)
    print
