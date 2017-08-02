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
    easy_ec2.py ip list [--debug|-d]
    easy_ec2.py ip alloc [--debug|-d]
    easy_ec2.py ip bind <instance_id> <elastic_ip> [--debug|-d]
    easy_ec2.py sec-group list [--debug|-d]
    easy_ec2.py sec-group create <group-name> [--description=<description>] [--debug|-d]
    easy_ec2.py sec-group delete <group-name>
    easy_ec2.py sec-group ingress <group-name> <protocol> <port_range>
    easy_ec2.py sec-group egress <group-name> <protocol> <port_range>
    easy_ec2.py sec-group attach <group-name> <instance_id>
    easy_ec2.py ansible playbook <instance_id> <playbook_file>
    easy_ec2.py s3 ls [<bucket>] [--debug|-d]
    easy_ec2.py s3 cp <from_file> <to_file> [--debug|-d]
    easy_ec2.py s3 share <s3_bucket_file> [--debug|-d]
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

class EasyEC2:

    def list_images( self, image_id = "", os="" ):
        return ["Not implement"]
    def create_tags( self, resource_id, tags ):
        return "Not implement"
    def delete_tags( self, resource_id, tags ):
        return "Not implement"

class EucaEasyEC2( EasyEC2 ):
    def __init__( self, config ):
        self.config = config
        
    def _exec_command( self, cmd ):        
        try:
            cmd.append( '-I' )
            cmd.append( self.config['access_id'] )
            cmd.append( '-S' )
            cmd.append( self.config['access_key'] )
            cmd.append( '--show-empty-fields' )
            if self.config['debug']:
                cmd.append( '--debug' )
            out = subprocess.check_output( cmd )
            if self.config['debug']:
                print "Command Execute result:"
                print "========================"
                print out
            return out
        except Exception, err:
            print err
            return ""
    def list_images( self, image_id = "", os=""):
        result = []
        cmd = ["euca-describe-images" ]
        if image_id:
            cmd.append( image_id )
        else:
            cmd.append( "-a" )
        out = self._exec_command( cmd )
    
        for line in out.split("\n"):
            words = line.split()
            if len(words) >= 13:
                if not os or words[2].find( os ) != -1:
                    result.append( {"image_id": words[1], "os": words[2], "format": words[12]} )
        return result

    def _find_image_id( self, name ):
        all_images = self.list_images()
        for image in all_images:
            if name == image['image_id']:
                return name
        for image in all_images:
            if image['os'].find( name ) != -1:
                return image['image_id']
        return ""

    def create_tags( self, resource_id, tags ):
        """
        create tag on the instance or volume
        """
        cmd = ["euca-create-tags",resource_id]
        for tag in tags:
            cmd.append( "--tag" )
            cmd.append( tag )
        out = self._exec_command( cmd )
        print out

    def delete_tags( self, resource_id, tags ):
        """delete the tags"""
        cmd = ["euca-delete-tags",resource_id ]
        for tag in tags:
            cmd.append( "--tag")
            cmd.append( tag )
        out = self._exec_command( cmd )
        print out

    def get_instances_by_tags( tags = None ):
        """
        get all the instances by the tags
        Return: a list of intance with the specified tags
        """
        instances = self.list_instances()
        if not tags:
            return instances
    
        result = []
        for inst in instances:
            if 'tags' in inst and set( tags ).issubset( set( inst['tags'] ) ):
                result.append( inst )
        return result

    def start_instance( self, image_id = 'emi-c1030eab', instance_type = 'm1.large', tags = None, zone=None ):
        real_image_id = self._find_image_id( image_id )
        if not real_image_id:
            print "Error: fail to find image by %s" % image_id
        if not zone:
            zone = self.get_first_available_zone( )
        out = self._exec_command( ["euca-run-instances", real_image_id, "-t", instance_type, '-z', zone, '-k', self.config['key_pair'] ] )
        result = self._parse_instance( out )
        if result and result[0]["instance_id"]:
            self.create_tags( result[0]["instance_id"], tags )
            instances = self.list_instances()
            for inst in instances:
                if inst['instance_id'] == result[0]['instance_id']:
                    return inst
        return result[0]

    def stop_instance( self, instance_id, force = False ):
        inst = self.find_instance( instance_id )
        if not inst:
            print "Fail to find instance %s" % instance_id
            return
        cmd = ['euca-stop-instances', inst['instance_id'] ]
        if force:
            cmd.append( '-f' )
        out = self._exec_command( cmd )
        print out

    def _parse_instance(self, out ):
        result = []
        for line in out.split( "\n"):
            words = line.split()
            if len( words ) >= 16 and words[0] == 'INSTANCE':
                inst = {"instance_id": words[1],
                        'image_id': words[2],
                        'public_host': words[3],
                        'private_host': words[4],
                        'state': words[5],
                        'key_pair': words[6],
                        'type': words[9],
                        'create_time': words[10],
                        'zone': words[11],
                        'monitoring': words[15],
                        'public_ip': words[16],
                        'private_ip': words[17],
                        'monitoring': words[11]}
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

    def list_instances( self, name = "" ):
        out = self._exec_command( ["euca-describe-instances" ] )
        instances = self._parse_instance( out )
        if not name:
            return instances
    
        result = []
    
        for inst in instances:
            if 'tags' in inst and ("name=%s"% name) in inst['tags']:
                result.append( inst )
        return result

    def find_instance( self, instance_id ):
        instances = self.list_instances()
        for inst in instances:
            if inst['instance_id'] == instance_id and inst['state'] == 'running':
                return inst 
            if 'tags' in inst and ('name=%s' % instance_id ) in inst['tags'] and inst['state'] == 'running':
                return inst
    
        return None

    def terminate_instance( self, instance_id ):
        inst = self.find_instance( instance_id )
        if not inst:
            print "Fail to find the instance %s" % instance_id
        result = {}
        out = self._exec_command( ["euca-terminate-instances", inst['instance_id'] ])
        for line in out.split("\n"):
            words = line.split()
            if len( words ) == 4 and words[0] == "INSTANCE":
                result["instance"] = words[1]
                result["state_from"] = words[2]
                result["state_to"] = words[3]
        return result

    def list_instance_types( self ):
        out = self._exec_command( ['euca-describe-instance-types'] )
        result = []
        for line in out.split("\n"):
            words = line.split()
            if len( words ) == 5 and words[0] == "INSTANCETYPE":
                result.append( {'name': words[1],
                                'cpu': words[2],
                                'memory': words[3],
                                'disk': words[4] } )
        return result

    def ssh( self, name ):
        instances = self.list_instances()
        for inst in instances:
            if ("name=%s" % name) in inst['tags'] or inst['instance_id'] == name:
                os.system("ssh -i %s -o StrictHostKeyChecking=no root@%s" % (self.config['key_pair_file'], inst['public_ip'] ) )

    def _get_public_ip( self, name, instances ):
        """
        get the public IP address by the name
        """
        for inst in instances:
            if ( "name=%s" % name ) in inst['tags'] or inst['instance_id'] == name:
                return inst['public_ip']
        return name

    def _create_remote_file_info( self, remoteFile, instances ):
        tmp = remoteFile.split( ":" )
        if len( tmp ) == 1:
            return tmp[0]
        elif len( tmp ) == 2:
            return "root@%s:%s" % ( _get_public_ip( tmp[0], instances ), tmp[1] )
        return ""

    def scp( self, from_file, to_file ):
        instances = self.list_instances()
        os.system( "scp -i %s -o StrictHostKeyChecking=no %s %s" % ( self.config['key_pair_file'], create_remote_file_info( from_file, instances ), create_remote_file_info( to_file, instances ) ) )

    def list_zones( self ):
        out = self._exec_command( ["euca-describe-availability-zones" ] )
        result =[] 
        for line in out.split( "\n" ):
            words = line.split()
            if len( words ) >= 3 and words[0] == "AVAILABILITYZONE":
                result.append( {'zone': words[1], 'state': words[2]} )
        return result

    def get_first_available_zone( self ):
        zones = self.list_zones()
        for zone_info in zones:
            if zone_info['state'] == 'available':
                return zone_info['zone']
        return ""

    def list_volumes( self, volume_id = None ):
        cmd = ["euca-describe-volumes" ]
        if volume_id:
            cmd.append( volume_id )
        out = self._exec_command( cmd )
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
            if len( words ) == 9 and words[0] == "VOLUME":
                volume_info = find_volume_info( words[1] )
                volume_info['size'] = words[2]
                volume_info['zone'] = words[4]
                volume_info['state'] = words[5]
                volume_info['create-time'] = words[6]
                volume_info['format'] = words[7]
            elif len( words ) == 5 and words[0] == "TAG":
                volume_info = find_volume_info( words[2] )
                if not 'tags' in volume_info:
                    volume_info['tags'] = {}
                volume_info['tags'][words[3]] = words[4]
            elif len( words ) == 6 and words[0] == "ATTACHMENT":
                volume_info = find_volume_info( words[1] )
                volume_info['attach'] = parse_volume( line )
    
        if volume_id and result:
            return result[0]
        else:
            return result

    def create_volume( self, size, zone = None, name = None ):
        if not zone:
            zone = self.get_first_available_zone( )
        cmd = ["euca-create-volume", "-z", zone, "-s", size, ]
        out = self._exec_command( cmd )
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
            self.create_tags( volume_info['id'], ["name=%s" % name] )
            return self.list_volumes( volume_info['id'] )
        else:
            return volume_info

    def delete_volume( self, volume_id ):
        volume_info = self.find_volume(volume_id )
        if volume_info:
            out = self._exec_command( ['euca-delete-volume', volume_info['id'] ] )
            print out
    def find_volume( self, volume_id ):
        volumes = self.list_volumes( )
        for volume_info in volumes:
            if (volume_info['id'] == volume_id or 
                'tags' in volume_info and 
                'name' in volume_info['tags'] and 
                volume_info['tags']['name'] == volume_id):
                return volume_info
        return None

    def attach_volume( self, instance_id, volume_id, device='/dev/vdc' ):
        instance = self.find_instance( instance_id )
        volume = self.find_volume( volume_id )
        if not instance:
            print "No such instance %s" % instance_id
        elif not volume:
            print "No such volume %s" % volume_id
        else:
            out = self._exec_command( ["euca-attach-volume", "-i", instance['instance_id'], "-d", device, volume['id'] ])
            return self._parse_volume( out )

    def detach_volume( self, volume_id, force = False ):
        volume = self.find_volume( volume_id )
        if not volume:
            print "No such volume %s" % volume_id
        else:
            cmd = ["euca-detach-volume", volume['id'] ]
            if force:
                cmd.append( '-f' )
            out = self._exec_command( cmd )
            return self._parse_volume( out )

    def _parse_volume( self, out ):
        words = out.split()
        if len( words ) == 6 and words[0] == 'ATTACHMENT':
            return {'volume': words[1],
                'instance-id': words[2],
                'attach-device': words[3],
                'state': words[4],
                'attach-time': words[5] }
        return {}

    def s3_copy( self, from_file, to_file ):
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
                inst = self.find_instance( host )
                if inst:
                    os.system( "ssh -i %s root@%s s3cmd get %s %s" % ( self.config['key_pair_file'], inst['public_ip'], from_file, to_file[to_file.find( ':' ) + 1:] ) )
                else:
                    print "no host %s is found" % host
            else: # copy the s3 file to local
                os.system( "s3cmd get %s %s" % (from_file, to_file) )
        elif to_file.startswith( "s3://"):
            if from_file.find( ':' ) != -1: #try to put remote file to s3
                host = from_file[0:from_file.find( ':') ]
                inst = self.find_instance( host )
                if inst:
                    os.system( "ssh -i %s root@%s s3cmd put %s %s" % ( self.config['key_pair_file'], inst['public_ip'], from_file[from_file.find( ':' ) + 1: ], to_file ) )
            else: # try to put local to s3
                os.system( "s3cmd put %s %s" % ( from_file, to_file) )


    def s3_share( self, s3_bucket_file ):
        """
        share the s3 file to public in the cloud
        """
        os.system( "s3cmd -P setacl %s" % s3_bucket_file )

    def s3_ls( self, bucket = None ):
        """
        list all the files under the s3_backet
        """
        if bucket:
            os.system( "s3cmd ls %s" % bucket )
        else:
            os.system( "s3cmd ls" )

    def elastic_ip_list( self ):
        cmd = ['euca-describe-addresses']
        print self._exec_command( cmd )

    def elastic_ip_bind( self, instance_id, elastic_ip ):
        inst = self.find_instance( instance_id )
        if inst:
            cmd = ['euca-associate-address', '-i', inst['instance_id'], elastic_ip ]
            print self._exec_command( cmd )
        else:
            print "fail to find instance by %s" % instance_id

    def list_sec_group( self ):
        cmd = ['euca-describe-group']
        print self._exec_command( cmd )

    def create_sec_group( self, name, desc = "no description" ):
        cmd = ['euca-create-group', name, '-d', desc ]
        print self._exec_command( cmd )

    def add_sec_group_ingress_rule( self, group_name, protocol, port_range ):
        cmd = ['euca-authorize', group_name, '-P', protocol, '-p', port_range ]
        print self._exec_command( cmd )

    def add_sec_group_egress_rule( self, group_name, protocol, port_range ):
        cmd = ['euca-authorize', group_name, '--egress', '-P', protocol, '-p', port_range ]
        print self._exec_command( cmd )

    def attach_sec_group( self, group_name, instance_id ):
        inst = self.find_instance( instance_id )
        if inst:
            cmd = ['euca-modify-instance-attribute', '-g', group_name, inst['instance_id'] ]
            print self._exec_command( cmd )
        else:
            print "Fail to find instance by id or name:%s" % instance_id
    def version( self ):
        return self._exec_command( ["euca-version"] )

    def create_keypair( self, name ):
        key_file = "%s.pem" % name
        result = []
        if os.path.exists( key_file ):
            sys.stdout.write( "the file %s exists, are you sure to overwrite it for keypair store?(Y/Yes):" % key_file )
            answer = sys.stdin.readline().strip()
        else:
            answer = "Y"
        if answer == "Y" or answer == "Yes":
            out = self._exec_command( ['euca-create-keypair', name, '-f', "%s.pem" % name ] )
            result = self._parse_keypairs( out )
        return result
    
    def delete_keypair( self, name ):
        print self._exec_command( ['euca-delete-keypair', name ] )
    
    def list_keypairs( self ):
        out = self._exec_command ( ['euca-describe-keypairs' ])
        return self._parse_keypairs( out )
    
    def _parse_keypairs( self, keypairs_out ):
        result = []
        for line in keypairs_out.split( "\n" ):
            words = line.split()
            if len( words ) == 3 and words[0] == "KEYPAIR":
                result.append( {'name': words[1], 'fingerprint': words[2] } )
        return result
    
    def create_ansible_hosts( self, instance_id ):
        inst = self.find_instance( instance_id )
        ansible_hosts_file = ".ansible_hosts"
        if not inst:
            print "Fail to find the instance %s" % instance_id
            return ""
        else:
            with open( ansible_hosts_file, "w" ) as fp:
                fp.write( "[dockers]\n")
                fp.write( "%s ansible_user=%s ansible_ssh_private_key_file=%s\n" % (inst['public_ip'], "root", self.config['key_pair_file']) )
            return ansible_hosts_file


    def ansible_playbook( self, instance_id, playbook_file ):
        ansible_hosts_file = self.create_ansible_hosts( instance_id )
        if ansible_hosts_file:
            os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
            os.environ['ANSIBLE_INVENTORY'] = os.path.abspath(ansible_hosts_file)
            os.system( "ansible-playbook %s" % playbook_file )
                
def printAsJson( o ):
    print json.dumps( o, indent = 4 )

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



def load_euca_config( ):
    euca_config = load_euca_ini( find_euca_ini() )
    config = {}
    if euca_config:
        config['access_id'] = get_from_euca_config( euca_config, 'key-id' )
        config['access_key'] = get_from_euca_config( euca_config, 'secret-key' )
        config['key_pair'] = find_key_pair()
        config['key_pair_file'] = find_key_pair_file()
    return config
    
def createEasyEC2( args ):
    config = load_euca_config()
    if config:
        if args['--debug'] or args['-d']:
            config['debug'] = True
        else:
            config['debug'] = False
        return EucaEasyEC2( config )
    return EasyEC2()
    
def main():
    args = docopt.docopt( __doc__, version="1.0" )    
    easy_ec2 = createEasyEC2( args )
    if args['image']:
        if args['list']:
            printAsJson( easy_ec2.list_images( args['--id'], args['--os'] ))
    elif args['instance']:
        if args['start']:
            inst_type = args['--type'] or "m1.large"
            zone = args['--zone'] or easy_ec2.get_first_available_zone()
            printAsJson( easy_ec2.start_instance( args['<image_id>'], inst_type, ["name=%s" % args['<name>']], zone = zone ) )
        elif args['list']:
            printAsJson( easy_ec2.list_instances( args['--name'] ))
        elif args['terminate']:
            printAsJson( easy_ec2.terminate_instance(  args['<instance_id>']))
        elif args['stop']:
            easy_ec2.stop_instance( args['<instance_id>'], args['--force'] )
        elif args['types']:
            printAsJson( easy_ec2.list_instance_types() )
    elif args['zone']:
        if args['list']:
            printAsJson( easy_ec2.list_zones( ) )
    elif args['tags']:
        if args['create']:
            easy_ec2.create_tags( args['<resource_id>'], args['<tag>'] )
        elif args['delete']:
            easy_ec2.delete_tags( args['<resource_id>'], args['<tag>'] )
    elif args['volume']:
        if args['list']:
            printAsJson( easy_ec2.list_volumes( args["--id"] ) )
        elif args['create']:
            easy_ec2.create_volume( args['<size>'], zone = args['--zone'], name=args['--name'] )
        elif args['delete']:
            easy_ec2.delete_volume( args['<volume_id>'])
        elif args['attach']:
            printAsJson( easy_ec2.attach_volume( args['<instance_id>'], args['<volume_id>'], args['--device'] or '/dev/vdc' ) )
        elif args['detach']:
            printAsJson( easy_ec2.detach_volume( args['<volume_id>'], args["--force"] ) )
    elif args['keypair']:
        if args['create']:
            printAsJson( easy_ec2.create_keypair( args['<name>']) )
        elif args['delete']:
            easy_ec2.delete_keypair( args['<name>'])
        elif args['list']:
            printAsJson( easy_ec2.list_keypairs() )
    elif args['ansible']:
        if args['playbook']:
            easy_ec2.ansible_playbook( args['<instance_id>'], args['<playbook_file>'] )
    elif args['s3']:
        if args['cp']:
            easy_ec2.s3_copy( args['<from_file>'], args['<to_file>'] )
        elif args['share']:
            easy_ec2.s3_share( args['<s3_bucket_file>'])
        elif args['ls']:
            easy_ec2.s3_ls( bucket=args['<bucket>'])
    elif args['ip']:
        if args['list']:
            easy_ec2.elastic_ip_list()
        elif args['bind']:
            easy_ec2.elastic_ip_bind( args['<instance_id>'], args['<elastic_ip>'])
    elif args['sec-group']:
        if args['list']:
            easy_ec2.list_sec_group( )
        elif args['create']:
            easy_ec2.create_sec_group( args['<group-name>'], desc = args['--description'] )
        elif args['ingress']:
           easy_ec2.add_sec_group_ingress_rule( args['<group-name>'], args['<protocol>'], args['<port_range>'] )
        elif args['egress']:
            easy_ec2.add_sec_group_egress_rule( args['<group-name>'], args['<protocol>'], args['<port_range>'] )
        elif args['attach']:
            easy_ec2.attach_sec_group( args['<group-name>'], args['<instance_id>'] )
    elif args['ssh']:
        easy_ec2.ssh( args['<name>'] )
    elif args['scp']:
        easy_ec2.scp( args['<from_file>'], args['<to_file>'] )
    elif args['version']:
        print easy_ec2.version();    



if __name__ == "__main__":
    main()
