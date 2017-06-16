# easy-ec2
a python program for easy the ec2 usage in Eucalyptus cloud environment

### install the euca2ools

in ubuntu:

```shell
$ sudo apt install euca2ools
```

### .ini file for euca2ools

copy the euca2ools .ini file to ~/.euca

### key-pair .pem file

copy the key-pair file to the ~/.euca

### run the easy_ec2 commands

#### get help

```shell
$ easy_ec2.py
```

#### list the available images

```shell
$ easy_ec2.py list images
```

#### start a instance

```shell
$ easy_ec2.py instance start <image_id> <name>
```

#### list all the instances

```shell
$ easy_ec2.py instance list
```
