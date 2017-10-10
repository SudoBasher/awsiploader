# AWS IP Loader

Use this to quickly add your IP to a couple of AWS security groups.

Setup these two files:

* config_credentials.py
* config_general.py

To add your current IP to your security groups:

```python aws_ip_loader.py```
or
```python aws_ip_loader.py add```

To remove your current IP to your security groups:

```python aws_ip_loader.py delete```
