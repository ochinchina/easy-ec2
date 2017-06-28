#!/usr/bin/python

"""
ec2 tool for manage the virtual machine in the EE-cloud

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
    easy_ec2.py s3 cp <from_file> <to_file> [--debug|-d]
    easy_ec2.py ssh <name> [--debug|-d]
    easy_ec2.py scp <from_file> <to_file> [--debug|-d]
    easy_ec2.py version 

Options:
"""

import sys
import os
import argparse
import subprocess
import json
import docopt
import ConfigParser 

def exec_command( config, cmd ):
    try:
        cmd.append( '-I' )
        cmd.append( config['access_id'] )
        cmd.append( '-S' )
        cmd.append( config['access_key'] )
        if config['debug']:
            cmd.append( '--debug' )
        return subprocess.check_output( cmd )
    except:
        return ""
def list_images( config, image_id = "", os=""):
    result = []
    cmd = ["euca-describe-images" ]
    if image_id:
        cmd.append( image_id )
    else:
        cmd.append( "-a" )
    out = exec_command( config, cmd )

    for line in out.split("\n"):
        words = line.split()
        if len(words) == 10:
            if os:
                if  words[2].find( os ) != -1:
                    result.append( {"image_id": words[1], "os": words[2], "format": words[9]} )
            else:
                result.append( {"image_id": words[1], "os": words[2], "format": words[9]} )
    return result

def find_image_id( config, name ):
    all_images = list_images( config )
    for image in all_images:
        if name == image['image_id']:
            return name
    for image in all_images:
        if image['os'].find( name ) != -1:
            return image['image_id']
    return ""

def create_tags( config, resource_id, tags ):
    """
    create tag on the instance or volume
    """
    cmd = ["euca-create-tags",resource_id]
    for tag in tags:
        cmd.append( "--tag" )
        cmd.append( tag )
    out = exec_command( config, cmd )
    print out

def delete_tags( config, resource_id, tags ):
    """delete the tags"""
    cmd = ["euca-delete-tags",resource_id ]
    for tag in tags:
        cmd.append( "--tag")
        cmd.append( tag )
    out = exec_command( config, cmd )
    print out

def get_instances_by_tags( config, tags = None ):
    """
    get all the instances by the tags
    Return: a list of intance with the specified tags
    """
    instances = list_instances( config )
    if not tags:
        return instances

    result = []
    for inst in instances:
        if 'tags' in inst and set( tags ).issubset( set( inst['tags'] ) ):
            result.append( inst )
    return result

def start_instance( config, image_id = 'emi-c1030eab', instance_type = 'm1.large', tags = None, zone=None ):
    real_image_id = find_image_id( config, image_id )
    if not real_image_id:
        print "Error: fail to find image by %s" % image_id
    if not zone:
        zone = get_first_available_zone( config )
    out = exec_command( config, ["euca-run-instances", real_image_id, "-t", instance_type, '-z', zone, '-k', config['key_pair'] ] )
    result = parse_instance( out )
    if result and result[0]["instance_id"]:
        create_tags( config, result[0]["instance_id"], tags )
        instances = list_instances( config )
        for inst in instances:
            if inst['instance_id'] == result[0]['instance_id']:
                return inst
    return result[0]

def stop_instance( config, instance_id, force = False ):
    inst = find_instance( config, instance_id )
    if not inst:
        print "Fail to find instance %s" % instance_id
        return
    cmd = ['euca-stop-instances', inst['instance_id'] ]
    if force:
        cmd.append( '-f' )
    out = exec_command( config, cmd )
    print out

def parse_instance( out ):
    result = []
    for line in out.split( "\n"):
        words = line.split()
        if len( words ) >= 16 and words[0] == 'INSTANCE':
            inst = {"instance_id": words[1],
                    'image_id': words[2],
                    'public_ip': words[-5],
                    'private_ip': words[-4],
                    'state': words[5],
                    'type': words[7] }
            if len( words ) == 17:
                inst['type'] = words[8]
                inst['key_pair'] = words[6]
            result.append( inst )
        elif result and len(words) >= 4 and words[0] == "TAG" and words[1] == "instance":
            if result and not 'tags' in result[-1]:
                result[-1]['tags'] = []
            if len( words ) > 4:
                tag = '%s=%s' % (words[3], words[4] )
            else:
                tag = words[3]
            result[-1]['tags'].append( tag )
        elif len( words ) == 5 and words[0] == "BLOCKDEVICE":
            if not 'devices' in result[-1]:
                result[-1]['devices'] = []
            result[-1]['devices'].append( {'device': words[1], 'volume_id': words[2], 'attach-time': words[3], 'delete-on-terminate': words[4] } )
    return result

def list_instances( config, name = "" ):
    out = exec_command( config, ["euca-describe-instances" ] )
    instances = parse_instance( out )
    if not name:
        return instances

    result = []

    for inst in instances:
        if 'tags' in inst and ("name=%s"% name) in inst['tags']:
            result.append( inst )
    return result

def find_instance( config, instance_id ):
    instances = list_instances( config )
    for inst in instances:
        if inst['instance_id'] == instance_id:
            return inst 
        if 'tags' in inst and ('name=%s' % instance_id ) in inst['tags']:
            return inst
    return None

def terminate_instance( config, instance_id ):
    inst = find_instance( config, instance_id )
    if not inst:
        print "Fail to find the instance %s" % instance_id
    result = {}
    out = exec_command(config, ["euca-terminate-instances", inst['instance_id'] ])
    for line in out.split("\n"):
        words = line.split()
        if len( words ) == 4 and words[0] == "INSTANCE":
            result["instance"] = words[1]
            result["state_from"] = words[2]
            result["state_to"] = words[3]
    return result

def list_instance_types( config ):
    out = exec_command( config, ['euca-describe-instance-types'] )
    result = []
    for line in out.split("\n"):
        words = line.split()
        if len( words ) == 5 and words[0] == "INSTANCETYPE":
            result.append( {'name': words[1],
                            'cpu': words[2],
                            'memory': words[3],
                            'disk': words[4] } )
    return result

def ssh( config, name ):
    instances = list_instances( config )
    for inst in instances:
        if ("name=%s" % name) in inst['tags'] or inst['instance_id'] == name:
            os.system("ssh -i %s -o StrictHostKeyChecking=no root@%s" % (config['key_pair_file'], inst['public_ip'] ) )

def get_public_ip( name, instances ):
    """
    get the public IP address by the name
    """
    for inst in instances:
        if ( "name=%s" % name ) in inst['tags'] or inst['instance_id'] == name:
            return inst['public_ip']
    return name

def create_remote_file_info( remoteFile, instances ):
    tmp = remoteFile.split( ":" )
    if len( tmp ) == 1:
        return tmp[0]
    elif len( tmp ) == 2:
        return "root@%s:%s" % ( get_public_ip( tmp[0], instances ), tmp[1] )
    return ""

def scp( config, from_file, to_file ):
    instances = list_instances(config)
    os.system( "scp -i %s -o StrictHostKeyChecking=no %s %s" % ( config['key_pair_file'], create_remote_file_info( from_file, instances ), create_remote_file_info( to_file, instances ) ) )

def list_zones( config ):
    out = exec_command( config, ["euca-describe-availability-zones" ] )
    result =[] 
    for line in out.split( "\n" ):
        words = line.split()
        if len( words ) == 3 and words[0] == "AVAILABILITYZONE":
            result.append( {'zone': words[1], 'state': words[2]} )
    return result

def get_first_available_zone( config ):
    zones = list_zones( config )
    for zone_info in zones:
        if zone_info['state'] == 'available':
            return zone_info['zone']
    return ""

def list_volumes( config, volume_id = None ):
    cmd = ["euca-describe-volumes" ]
    if volume_id:
        cmd.append( volume_id )
    out = exec_command( config, cmd )
    result = []
    def find_volume_info( volume_id ):
        for volume_info in result:
            if volume_info['id'] == volume_id:
                return volume_info
        volume_info = {'id': volume_id }
        result.append( volume_info )
        return volume_info
    for line in out.split( "\n"):
        words = line.split()
        if len( words ) == 7 and words[0] == "VOLUME":
            volume_info = find_volume_info( words[1] )
            volume_info['size'] = words[2]
            volume_info['zone'] = words[3]
            volume_info['state'] = words[4]
            volume_info['create-time'] = words[5]
            volume_info['format'] = words[6]
        elif len( words ) == 5 and words[0] == "TAG":
            volume_info = find_volume_info( words[2] )
            if not 'tags' in volume_info:
                volume_info['tags'] = {}
            volume_info['tags'][words[3]] = words[4]
        elif len( words ) == 6 and words[0] == "ATTACHMENT":
            volume_info = find_volume_info( words[1] )
            volume_info['attach'] = {'instance':words[2], 'device':words[3],'state':words[4],'time':words[5]}

    if volume_id and result:
        return result[0]
    else:
        return result

def create_volume( config, size, zone = None, name = None ):
    if not zone:
        zone = get_first_available_zone( config )
    cmd = ["euca-create-volume", "-z", zone, "-s", size, ]
    out = exec_command( config, cmd )
    volume_info = {}
    for line in out.split("\n"):
        words = line.split()
        if len( words ) >= 6 and words[0] == 'VOLUME':
            volume_info['id'] = words[1]
            volume_info['size'] = words[2]
            volume_info['zone'] = words[3]
            volume_info['state'] = words[4]
            volume_info['create-time'] = words[5]
    if name:
        create_tags( config, volume_info['id'], ["name=%s" % name] )
        return list_volumes( config, volume_info['id'] )
    else:
        return volume_info

def delete_volume( config, volume_id ):
    volume_info = find_volume( config, volume_id )
    if volume_info:
        out = exec_command( config, ['euca-delete-volume', volume_info['id'] ] )
        print out
def find_volume( config, volume_id ):
    volumes = list_volumes( config )
    for volume_info in volumes:
        if (volume_info['id'] == volume_id or 
            'tags' in volume_info and 
            'name' in volume_info['tags'] and 
            volume_info['tags']['name'] == volume_id):
            return volume_info
    return None

def attach_volume( config, instance_id, volume_id, device='/dev/vdc' ):
    instance = find_instance( config, instance_id )
    volume = find_volume( config, volume_id )
    if not instance:
        print "No such instance %s" % instance_id
    elif not volume:
        print "No such volume %s" % volume_id
    else:
        out = exec_command( config, ["euca-attach-volume", "-i", instance['instance_id'], "-d", device, volume['id'] ])
        print out

def detach_volume( config, volume_id, force = False ):
    volume = find_volume( config, volume_id )
    if not volume:
        print "No such volume %s" % volume_id
    else:
        cmd = ["euca-detach-volume", volume['id'] ]
        if force:
            cmd.append( '-f' )
        out = exec_command( config, cmd )
        print out

def s3_copy( config, from_file, to_file ):
    """
    copy the file from s3 to instance in cloud
    or copy the file from instance in cloud to s3
    """
    if from_file.startswith( "s3://" ):
        if to_file.startswith( "s3://"):
            os.system( "s3cmd cp %s %s" % (from_file, to_file) )
        elif to_file.find( ':' ) != -1:
            # extract the host
            host = to_file[0:to_file.find( ':') ]
            inst = find_instance( config, host )
            if inst:
                os.system( "ssh -i %s root@%s s3cmd get %s %s" % ( config['key_pair_file'], inst['public_ip'], from_file, to_file[to_file.find( ':' ) + 1:] ) )
            else:
                print "no host %s is found" % host
        else: # copy the s3 file to local
            os.system( "s3cmd get %s %s" % (from_file, to_file) )
    elif to_file.startswith( "s3://"):
        if from_file.find( ':' ) != -1: #try to put remote file to s3
            host = from_file[0:from_file.find( ':') ]
            inst = find_instance( config, host )
            if inst:
                os.system( "ssh -i %s root@%s s3cmd put %s %s" % ( config['key_pair_file'], inst['public_ip'], from_file[from_file.find( ':' ) + 1: ], to_file ) )
        else: # try to put local to s3
            os.system( "s3cmd put %s %s" % ( from_file, to_file) )


def printAsJson( o ):
    print json.dumps( o, indent = 4 )

def main():
    args = docopt.docopt( __doc__, version="1.0" )
    config = load_config()
    if args['--debug'] or args['-d']:
        config['debug'] = True
    else:
        config['debug'] = False
    if args['image']:
        if args['list']:
            printAsJson(list_images( config, args['--id'], args['--os'] ))
    elif args['instance']:
        if args['start']:
            inst_type = args['--type'] or "m1.large"
            zone = args['--zone'] or get_first_available_zone(config)
            printAsJson(start_instance(config, args['<image_id>'], inst_type, ["name=%s" % args['<name>']], zone = zone ) )
        elif args['list']:
            printAsJson(list_instances( config, args['--name'] ))
        elif args['terminate']:
            printAsJson(terminate_instance( config, args['<instance_id>']))
        elif args['stop']:
            stop_instance( config, args['<instance_id>'], args['--force'] )
        elif args['types']:
            printAsJson( list_instance_types( config ) )
    elif args['zone']:
        if args['list']:
            printAsJson( list_zones( config ) )
    elif args['tags']:
        if args['create']:
            create_tags( config, args['<resource_id>'], args['<tag>'] )
        elif args['delete']:
            delete_tags( config, args['<resource_id>'], args['<tag>'] )
    elif args['volume']:
        if args['list']:
            printAsJson( list_volumes( config, args["--id"] ) )
        elif args['create']:
            create_volume( config, args['<size>'], zone = args['--zone'], name=args['--name'] )
        elif args['delete']:
            delete_volume( config, args['<volume_id>'])
        elif args['attach']:
            attach_volume( config, args['<instance_id>'], args['<volume_id>'], args['--device'] or '/dev/vdc' )
        elif args['detach']:
            detach_volume( config, args['<volume_id>'], args["--force"] )
    elif args['keypair']:
        if args['create']:
            printAsJson( create_keypair( config, args['<name>']) )
        elif args['delete']:
            delete_keypair( config, args['<name>'])
        elif args['list']:
            printAsJson( list_keypairs( config ) )
    elif args['ansible']:
        if args['playbook']:
            ansible_playbook( config, args['<instance_id>'], args['<playbook_file>'] )
    elif args['s3']:
        if args['cp']:
            s3_copy( config, args['<from_file>'], args['<to_file>'] )
    elif args['ssh']:
        ssh( config, args['<name>'] )
    elif args['scp']:
        scp( config, args['<from_file>'], args['<to_file>'] )
    elif args['version']:
        os.system( "euca-version -I %s -S %s" % ( config['access_id'], config['access_key']) )
    #print json.dumps( list_images( config ), indent = 4 )
    #print json.dumps( list_instances( config ), indent = 4 )
    #create_tags( config, 'i-95928170', ['type=taf', 'instance=taf1'])

def load_euca_ini( eucaIniFile ):
    config = ConfigParser.ConfigParser()
    config.read( [eucaIniFile])
    return config

def get_from_euca_config( euca_config, key ):
    for section in euca_config.sections():
        for item in euca_config.items( section ):
            if item[0] == key:
                return item[1]
    return ""

def find_file_with_suffix_in_directory( dirName, suffix ):
    result = []
    if os.path.isdir( dirName ):
        files = os.listdir( dirName )
        for f in files:
            if os.path.isfile( dirName + '/' + f ) and f.endswith( suffix ):
                result.append( dirName + '/' + f )
    return result

def find_euca_ini():
    if os.path.isfile( '/etc/euca2ools/euca2ools.ini' ):
        return '/etc/euca2ools/euca2ools.ini'
    files = find_file_with_suffix_in_directory( '/etc/euca2ools/conf.d', ".ini")
    if not files :
        files = find_file_with_suffix_in_directory( os.path.expanduser('~/.euca' ), ".ini")
    if files:
        return files[0]
    else:
        return ""

def find_key_pair():
    key_pair_file = find_key_pair_file()
    if key_pair_file:
        return os.path.basename( key_pair_file )[:-4]
    return ""

def find_key_pair_file():
    files = find_file_with_suffix_in_directory( os.path.expanduser('~/.euca' ), ".pem")
    for f in files:
        name = os.path.basename( f )
        if (name.endswith( ".pem" ) and 
                not name.startswith( "euca2-" ) and 
                not name.endswith( "cert.pem") and
                not name.endswith( "pk.pem" ) ):
            return f
    return ""

def create_keypair( config, name ):
    key_file = "%s.pem" % name
    result = []
    if os.path.exists( key_file ):
        sys.stdout.write( "the file %s exists, are you sure to overwrite it for keypair store?(Y/Yes):" % key_file )
        answer = sys.stdin.readline().strip()
        if answer == "Y" or answer == "Yes":
            out = exec_command( config, ['euca-create-keypair', name, '-f', "%s.pem" % name ] )
            result = parse_keypairs( out )
    return result

def delete_keypair( config, name ):
    print exec_command( config, ['euca-delete-keypair', name ] )

def list_keypairs( config ):
    out = exec_command ( config, ['euca-describe-keypairs' ])
    return parse_keypairs( out )

def parse_keypairs( keypairs_out ):
    result = []
    for line in keypairs_out.split( "\n" ):
        words = line.split()
        if len( words ) == 3 and words[0] == "KEYPAIR":
            result.append( {'name': words[1], 'fingerprint': words[2] } )
    return result

def create_ansible_hosts( config, instance_id ):
    inst = find_instance( config, instance_id )
    ansible_hosts_file = ".ansible_hosts"
    if not inst:
        print "Fail to find the instance %s" % instance_id
        return ""
    else:
        with open( ansible_hosts_file, "w" ) as fp:
            fp.write( "[dockers]\n")
            fp.write( "%s ansible_user=%s ansible_ssh_private_key_file=%s\n" % (inst['public_ip'], "root", config['key_pair_file']) )
        return ansible_hosts_file


def ansible_playbook( config, instance_id, playbook_file ):
    ansible_hosts_file = create_ansible_hosts( config, instance_id )
    if ansible_hosts_file:
        os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
        os.environ['ANSIBLE_INVENTORY'] = os.path.abspath(ansible_hosts_file)
        os.system( "ansible-playbook %s" % playbook_file )

def load_config( ):
    euca_config = load_euca_ini( find_euca_ini() )
    config = {}
    config['access_id'] = get_from_euca_config( euca_config, 'key-id' )
    config['access_key'] = get_from_euca_config( euca_config, 'secret-key' )
    config['key_pair'] = find_key_pair()
    config['key_pair_file'] = find_key_pair_file()
    return config

if __name__ == "__main__":
    main()
