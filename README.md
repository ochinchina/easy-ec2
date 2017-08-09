# easy-ec2

A lot of useful script in the euca2ools is provided by the Eucalyptus. It is a little bit hard to remember these commands. To relief this pain, this tool written in python is introduced. Often used commands are integrated into this script. You can only run this script to execute the commands in euca2ools. If not clear about the command, you can simply run this tool without any command line arguments and this tool will print the help menu in the console.

This script also supports the openstack client.

Except for wrapping the commands in the euca2ools, this tools also provides:

- ssh integration
- scp integration
- ansible integration

### install the euca2ools

in ubuntu:

```shell
$ sudo apt install euca2ools
```

### install python-openstackclient

in ubuntu
```shell
$ sudo pip install python-openstackclient
```

#### .ini file for euca2ools

copy the euca2ools .ini file to ~/.euca

### .ini file for openstack

get your openstack rc file and execute the script like:

```shell
$ /your/openstack/rc.sh
```

the above script requires you input a password and please input your password when prompt, and then list all the openstack environment variable and put to the ~/.openstack/openstack.ini file "AUTH" section like:

```shell
$ echo "[AUTH]" >~/.openstack/openstack.ini
$ env | grep OS_ >&~/.openstack/openstack.ini
```

after executing above script, the contents of file looks like:

```text
[AUTH]
OS_AUTH_URL=<url-to-openstack-identity>
OS_REGION_NAME=<your-region>
OS_PROJECT_NAME=<project-name>
OS_USER_DOMAIN_NAME=<user-domain-name>
OS_IDENTITY_API_VERSION=3
OS_INTERFACE=public
OS_PASSWORD=<password>
OS_USERNAME=<username>
OS_PROJECT_ID=<project-id>
```

you also need to add a section "DEFAULT" to the file ~/.openstack/openstack.ini with following keys:

- public_network: the public network in your openstack cloud
- dns_servers: the dns servers for internet access
- default_instance_type: the default instance type if no instance type is provided when start instance

After adding above parameters into file ~/.openstack/openstack.ini, the contents of ~/.openstack/openstack.ini looks like:

```text
[AUTH]
OS_AUTH_URL=<url-to-openstack-identity>
OS_REGION_NAME=<your-region>
OS_PROJECT_NAME=<project-name>
OS_USER_DOMAIN_NAME=<user-domain-name>
OS_IDENTITY_API_VERSION=3
OS_INTERFACE=public
OS_PASSWORD=<password>
OS_USERNAME=<username>
OS_PROJECT_ID=<project-id>

[DEFAULT]

public_network=<public-network>
dns_servers= <dns-servers-seperated-by-comma>
default_instance_type=m1.medium

```

#### key-pair .pem file

copy the key-pair file to the ~/.euca or ~/.openstack

### run the easy-ec2 commands

#### Get help

```shell
$ easy_ec2.py
Usage:
    easy_ec2.py image list [--os=<os>] [--id=<image_id>] [--debug|-d]
    easy_ec2.py tags create <resource_id> [--debug|-d] [<tag>...]
    easy_ec2.py tags delete <resource_id> [--debug|-d] [<tag>...]
    easy_ec2.py instance start <image_id> <name> [--debug|-d] [--type=<type>] [--zone=<zone>]
    easy_ec2.py instance stop <instance_id> [--debug|-d] [--force]
    easy_ec2.py instance list [--debug|-d] [--name=<name>]
    easy_ec2.py instance terminate <instance_id> [--debug|-d]
    easy_ec2.py instance types [--debug|-d]
    easy_ec2.py zone list [--debug|-d]
    easy_ec2.py volume list [--id=<volume_id>] [--debug|-d]
    easy_ec2.py volume create <size> [--zone=<zone>] [--name=<name>] [--debug|-d]
    easy_ec2.py volume delete <volume_id> [--debug|-d]
    easy_ec2.py volume attach <instance_id> <volume_id> [--device=<device>] [--debug|-d]
    easy_ec2.py volume detach <volume_id> [--force] [--debug|-d]
    easy_ec2.py keypair create <name> [--debug|-d]
    easy_ec2.py keypair delete <name> [--debug|-d]
    easy_ec2.py keypair list [--debug|-d]
    easy_ec2.py ansible playbook <instance_id> <playbook_file>
    easy_ec2.py ssh <name> [--debug|-d]
    easy_ec2.py scp <from_file> <to_file> [--debug|-d]
    easy_ec2.py version
```

#### List the available images in the cloud

Before starting an instance, we need to know what images are available. The command "easy_ec2.py image list" will list all the available images in the cloud.

```shell
$ easy_ec2.py image list
[
    {
        "image_id": "emi-00598f81",
        "os": "eecloud-baseimages-linux-x86_64-2017-03-23/ubuntu-14.04.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-04d8e7d9",
        "os": "eecloud-baseimages-linux-x86_64-2016-08-23/rhel-5.7.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-04e61b6a",
        "os": "devhz2-fddps/devhz2-fddps-image-v0.8.0-prefix.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-07bb9ba8",
        "os": "eecloud-baseimages-linux-x86_64-2017-06-08/centos-6.9.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-07f33592",
        "os": "eecloud-baseimages-linux-x86_64-2017-05-08/fedora-24.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-0ac7ae43",
        "os": "eecloud-baseimages-linux-x86_64-2017-03-23/ubuntu-16.04.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-0b6521b8",
        "os": "eecloud-baseimages-linux-x86_64-2016-05-18/coreos-stable.img.manifest.xml",
        "format": "hvm"
    }
]

```

If only ubuntu images is listed, provide the optional command line argument "--os ubuntu" like:

```shell
$ easy_ec2.py image list --os ubuntu
[
    {
        "image_id": "emi-00598f81",
        "os": "eecloud-baseimages-linux-x86_64-2017-03-23/ubuntu-14.04.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-0ac7ae43",
        "os": "eecloud-baseimages-linux-x86_64-2017-03-23/ubuntu-16.04.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-1132aeef",
        "os": "eecloud-baseimages-linux-x86_64-2017-05-08/ubuntu-14.04.img.manifest.xml",
        "format": "hvm"
    },
    {
        "image_id": "emi-3b44ad04",
        "os": "eecloud-baseimages-linux-x86_64-2016-08-23/ubuntu-16.04.img.manifest.xml",
        "format": "hvm"
    }
]
```

#### List the available virtual machine type

The command "easy_ec2.py instance types" will list all the virtual machine type available in the cloud.

```shell
$ easy_ec2.py instance types

[
    {
        "disk": "25",
        "memory": "2048",
        "name": "t1.micro",
        "cpu": "1"
    },
    {
        "disk": "32",
        "memory": "8192",
        "name": "m1.small",
        "cpu": "2"
    },
    {
        "disk": "64",
        "memory": "16384",
        "name": "m1.medium",
        "cpu": "2"
    },
    {
        "disk": "64",
        "memory": "16384",
        "name": "c1.medium",
        "cpu": "4"
    },
    {
        "disk": "128",
        "memory": "24576",
        "name": "m1.large",
        "cpu": "4"
    },
    {
        "disk": "128",
        "memory": "24576",
        "name": "m1.xlarge",
        "cpu": "6"
    },
    {
        "disk": "192",
        "memory": "32768",
        "name": "c1.xlarge",
        "cpu": "6"
    },
    {
        "disk": "192",
        "memory": "32768",
        "name": "m2.xlarge",
        "cpu": "8"
    },
    {
        "disk": "256",
        "memory": "40960",
        "name": "m3.xlarge",
        "cpu": "8"
    },
    {
        "disk": "320",
        "memory": "51200",
        "name": "m2.2xlarge",
        "cpu": "10"
    },
    {
        "disk": "320",
        "memory": "51200",
        "name": "m3.2xlarge",
        "cpu": "12"
    },
    {
        "disk": "384",
        "memory": "61440",
        "name": "cc1.4xlarge",
        "cpu": "12"
    },
    {
        "disk": "384",
        "memory": "61440",
        "name": "m2.4xlarge",
        "cpu": "16"
    },
    {
        "disk": "512",
        "memory": "81920",
        "name": "hi1.4xlarge",
        "cpu": "16"
    },
    {
        "disk": "512",
        "memory": "81920",
        "name": "cc2.8xlarge",
        "cpu": "24"
    },
    {
        "disk": "768",
        "memory": "122880",
        "name": "cg1.4xlarge",
        "cpu": "24"
    },
    {
        "disk": "768",
        "memory": "122880",
        "name": "cr1.8xlarge",
        "cpu": "30"
    },
    {
        "disk": "1280",
        "memory": "204800",
        "name": "hs1.8xlarge",
        "cpu": "40"
    }
]

```

#### Start a virtual machine

The command "easy_ec2.py instance start <image_id> <name> [--type=<type>]" will start a virtual machine in the cloud with image and the specified type. If the "--type" command line argument is not provided, a "m1.large" will be created. The image_id can be the os name such as "ubuntu-16.04". The "name" command line argument will make a label on the virtual machine and can  be used in the following "ssh, scp and ansible" commands.

```shell
$ easy_ec2.py instance start ubuntu-16.04 test-1 --type m1.small

    {
        "public_ip": "10.10.1.215",
        "tags": [
            "name=test-1"
        ],
        "instance_id": "i-7c13c790",
        "image_id": "emi-0ac7ae43",
        "state": "running",
        "key_pair": "test_key_pair",
        "private_ip": "10.254.2.133",
        "type": "m1.small"
    }

```

#### List all the instances

To list all started virtual machine, simply run following commands
```shell
$ easy_ec2.py instance list
[
    {
        "public_ip": "10.10.1.215",
        "tags": [
            "name=test-1"
        ],
        "instance_id": "i-7c13c790",
        "image_id": "emi-0ac7ae43",
        "state": "running",
        "key_pair": "test_key_pair",
        "private_ip": "10.254.2.133",
        "type": "m1.small"
    }
]
```

#### ssh into the virtual machine

After the virtual machine is started, we can ssh to the virtual machine by the instance_id or name provided in the "instance start <image_id> <name>"

ssh by name
```shell
$ easy_ec2.py ssh test-1
```

ssh by instance id
```
$ easy_ec2.py ssh i-7c13c790
```

#### ansible playbook

This tool integrates with the ansible, so if want to manage the virtual machine with ansible, we can just simply execute:

```shell
$ easy_ec2.py ansible playbook test-1 software-install.yml
```

#### copy from/to s3

s3cmd is integrated into this tool. If s3cmd is installed and the related .s3cfg is configured in the virtual machine, this tool can copy from/to s3 file.

Download from s3 to host test-1:

```shell
$ easy_ec2.py s3 cp s3://some/file test-1:/root
```

upload file from host test-1 to s3:

```shell
$ easy_ec2.py s3 cp test-1:/root/test_file.gz s3://some/directory
```
