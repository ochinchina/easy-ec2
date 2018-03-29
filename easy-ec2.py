#!/usr/bin/python

"""
ec2 tool for manage the virtual machine in the EE-cloud

Usage:
    easy_ec2.py image list [--os=<os>] [--id=<image_id>] [--config_dir=<config_dir>] [--debug|-d]
    easy_ec2.py tags create <resource_id> [--debug|-d] [<tag>...] [--config_dir=<config_dir>]
    easy_ec2.py tags delete <resource_id> [--debug|-d] [<tag>...] [--config_dir=<config_dir>]
    easy_ec2.py instance start <image_id> <name> [--debug|-d] [--type=<type>] [--zone=<zone>] [--config_dir=<config_dir>]
    easy_ec2.py instance stop <instance_id> [--debug|-d] [--force] [--config_dir=<config_dir>]
    easy_ec2.py instance list [--debug|-d] [--name=<name>] [--config_dir=<config_dir>]
    easy_ec2.py instance terminate <instance_id> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py instance types [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py zone list [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py volume list [--id=<volume_id>] [--status=status] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py volume create <size> [--zone=<zone>] [--name=<name>] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py volume delete <volume_id> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py volume attach <instance_id> <volume_id> [--device=<device>] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py volume detach <instance_id> <volume_id> [--force] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py keypair create <name> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py keypair delete <name> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py keypair list [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip list [--free] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip alloc [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip alloc-attach <instance_id> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip delete <ip_addr> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip attach <instance_id> <elastic_ip> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ip detach <instance_id> <elastic_ip> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group list [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group create <group_name> [--description=<description>] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group delete <group_name> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group ingress <group_name> <protocol> <port_range> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group egress <group_name> <protocol> <port_range> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group attach <group_name> <instance_id> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py sec-group detach <group_name> <instance_id> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py network list [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py network create <network_name> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py subnet add <network_name> <subnet_name> <subnet_cidr> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py subnet list [--debug|-d] [--name=<subnet_name>] [--config_dir=<config_dir>]
    easy_ec2.py subnet remove <subnet_name> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py router list [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ansible playbook <instance_id> <playbook_file>... [--config_dir=<config_dir>]
    easy_ec2.py s3 ls [<bucket>] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py s3 cp <from_file> <to_file> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py s3 share <s3_bucket_file> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py ssh <name> [--user=user] [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py scp <from_file> <to_file> [--debug|-d] [--config_dir=<config_dir>]
    easy_ec2.py version [--debug|-d]

"""

import sys
import os
import subprocess
import json
import docopt
import ConfigParser 
import tempfile

class EasyEC2:

    def list_images( self, image_id = "", os="" ):
        return ["Not implement"]
    def list_instances( self, name = "" ):
        return "Not implement"
    def start_instance( self, image_id, name, instance_type, tags = None, zone=None ):
        return "Not implement"     
    def stop_instance( self, instance_id, force = False ):
        return "Not implement"
    def terminate_instance( self, instance_id ):
        return "Not implement"
    def list_instance_types( self ):
        return "Not implement"
    def elastic_ip_list( self, free = False ):
        return "Not implement"
    def create_elastic_ip( self ):
        return "Not implement"
    def elastic_ip_alloc_attach( self, instance_id ):
        return "Not implement"
    def elastic_ip_delete( self, ip_addr ):
        return "Not implement"
    def elastic_ip_attach( self, instance_id, elastic_ip ):
        return "Not implement"
    def create_tags( self, resource_id, tags ):
        return "Not implement"
    def delete_tags( self, resource_id, tags ):
        return "Not implement"
    def list_networks( self ):
        return "Not implement"
    def create_network( self, name ):
        return "Not implement"
    def add_subnet( self, network_name, subnet_name, subnet_cidr ):
        return "Not implement"
    def list_subnet( self, subnet_name ):
        return "Not implement"
    def remove_subnet( self, subnet_name ):
        return "Not implement"
    def delete_keypair( self, name ):
        return "Not implement" 
    def list_keypairs( self ):
        return "Not implement"
    def list_sec_group( self ):
        return "Not implement"
    def create_sec_group( self, name, desc = "no description" ):
        return "Not implement"
    def add_sec_group_ingress_rule( self, group_name, protocol, port_range ):
        return "Not implement"
    def add_sec_group_egress_rule( self, group_name, protocol, port_range ):
        return "Not implement"
    def attach_sec_group( self, group_name, instance_id ):
        return "Not implement"
    def list_volumes( self, volume_id = None, status = None ):
        return "Not implement"
    def create_volume( self, size, zone = None, name = None ):
        return "Not implement"
    def delete_volume( self, volume_id ):
        return "Not implement"
    def attach_volume( self, instance_id, volume_id, device='/dev/vdc' ):
        return "Not implement"
    def detach_volume( self, instance_id, volume_id, force = False ):
        return "Not implement"
    def list_zones( self ):
        return "Not implement"
    def ssh( self, name, user = "root" ):
        """
        login to the vm name with user name
        """
        return "Not implement"
    def s3_copy( self, from_file, to_file ):
        return "Not implement"
    def s3_share( self, s3_bucket_file ):
        """
        share the s3 file to public in the cloud
        """
        out = subprocess.check_output( ['s3cmd', 'ls', "-r", s3_bucket_file] )
        for line in out.strip().split("\n"):
            words = line.split()
            print words[3]
            os.system( "s3cmd -P setacl %s" % words[3] )


    def s3_ls( self, bucket = None ):
        """
        list all the files under the s3_backet
        """
        if bucket:
            os.system( "s3cmd ls %s" % bucket )
        else:
            os.system( "s3cmd ls" )
    def ansible_playbook( self, instance_id, playbook_file ):
        return "Not implemented"
    def _is_exec_file_exist( self, exec_file ):
        try:
            out = subprocess.check_output( ['which', exec_file ] ).strip()
            return os.path.isfile( out )
        except:
            return False

    def _download_s3file( self, s3_filename ):
        """
        download a file from s3 and save it to the temp directory

        Args:
            s3_filename - the name of s3 file
        Return:
            the temp local file name who hold the contents of s3 file
        """
        basename = os.path.basename( s3_filename[len("s3://"):] )
        filename = os.path.join( tempfile.mkdtemp(), basename )
        os.system( "s3cmd get -f %s %s" % (s3_filename, filename ) )
        return filename
            
class EucaEasyEC2( EasyEC2 ):
    def __init__( self, config ):
        self.config = config
        
    def _exec_command( self, cmd ):
        if not self._is_exec_file_exist( cmd[0] ):
            print( "executable file %s is not found, please install the euca2ools" % cmd[0] )
            return "executable file %s is not found" % cmd[0]
        try:
            cmd.append( '-I' )
            cmd.append( self.config['access_id'] )
            cmd.append( '-S' )
            cmd.append( self.config['access_key'] )
            cmd.append( '--show-empty-fields' )
            if self.config['debug']:
                cmd.append( '--debug' )
                print( "start to execute command:%s" % (" ".join( cmd ) ) )
            out = subprocess.check_output( cmd )
            if self.config['debug']:
                print("Command Execute result:")
                print("========================")
                print(out)
            return out
        except Exception as err:
            print(err)
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
        print(out)

    def delete_tags( self, resource_id, tags ):
        """delete the tags"""
        cmd = ["euca-delete-tags",resource_id ]
        for tag in tags:
            cmd.append( "--tag")
            cmd.append( tag )
        out = self._exec_command( cmd )
        print(out)

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

    def start_instance( self, image_id, name, instance_type, tags = None, zone=None ):
        real_image_id = self._find_image_id( image_id )
        if not real_image_id:
            print("Error: fail to find image by %s" % image_id)
            return
        if not zone:
            zone = self.get_first_available_zone( )
        if not tags:
            tags = []
        if not instance_type:
            instance_type = "m1.large"
            
        tags.append( "name=%s" % name )
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
            print("Fail to find instance %s" % instance_id)
            return
        cmd = ['euca-stop-instances', inst['instance_id'] ]
        if force:
            cmd.append( '-f' )
        out = self._exec_command( cmd )
        print(out)

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
            print("Fail to find the instance %s" % instance_id)
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

    def ssh( self, name, user  = "root"):
        instances = self.list_instances()
        if user is None or len( user ) <= 0: user = "root"
        for inst in instances:
            if ("name=%s" % name) in inst['tags'] or inst['instance_id'] == name:
                os.system("ssh -i %s -o StrictHostKeyChecking=no %s@%s" % (user, self.config['key_pair_file'], inst['public_ip'] ) )

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
            return "root@%s:%s" % ( self._get_public_ip( tmp[0], instances ), tmp[1] )
        return ""

    def scp( self, from_file, to_file ):
        instances = self.list_instances()
        os.system( "scp -i %s -o StrictHostKeyChecking=no %s %s" % ( self.config['key_pair_file'], self._create_remote_file_info( from_file, instances ), self._create_remote_file_info( to_file, instances ) ) )

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

    def list_volumes( self, volume_id = None, status = None ):
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
            print(out)
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
            print("No such instance %s" % instance_id)
        elif not volume:
            print("No such volume %s" % volume_id)
        else:
            out = self._exec_command( ["euca-attach-volume", "-i", instance['instance_id'], "-d", device, volume['id'] ])
            return self._parse_volume( out )

    def detach_volume( self, instance_id, volume_id, force = False ):
        volume = self.find_volume( volume_id )
        if not volume:
            print("No such volume %s" % volume_id)
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
                    print("no host %s is found" % host)
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

    def elastic_ip_list( self, free = False ):
        cmd = ['euca-describe-addresses']
        return self._exec_command( cmd )

    def elastic_ip_attach( self, instance_id, elastic_ip ):
        inst = self.find_instance( instance_id )
        if inst:
            cmd = ['euca-associate-address', '-i', inst['instance_id'], elastic_ip ]
            return self._exec_command( cmd )
        else:
            return "fail to find instance by %s" % instance_id
    def create_elastic_ip( self ):
        return "not implement"
    def elastic_ip_delete( self, ip_addr ):
        return "not implement"
    def list_sec_group( self ):
        cmd = ['euca-describe-group']
        return self._exec_command( cmd )

    def create_sec_group( self, name, desc = "no description" ):
        cmd = ['euca-create-group', name, '-d', desc ]
        return self._exec_command( cmd )

    def add_sec_group_ingress_rule( self, group_name, protocol, port_range ):
        cmd = ['euca-authorize', group_name, '-P', protocol, '-p', port_range ]
        return self._exec_command( cmd )

    def add_sec_group_egress_rule( self, group_name, protocol, port_range ):
        cmd = ['euca-authorize', group_name, '--egress', '-P', protocol, '-p', port_range ]
        return self._exec_command( cmd )
    def create_elastic_ip( self ):
        return "not implement"
    def elastic_ip_delete( self, ip_addr ):
        return "not implement"
    def list_sec_group( self ):
        cmd = ['euca-describe-group']
        return self._exec_command( cmd )

    def attach_sec_group( self, group_name, instance_id ):
        inst = self.find_instance( instance_id )
        if inst:
            cmd = ['euca-modify-instance-attribute', '-g', group_name, inst['instance_id'] ]
            return self._exec_command( cmd )
        else:
            return "Fail to find instance by id or name:%s" % instance_id
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
        print(self._exec_command( ['euca-delete-keypair', name ] ))
    
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
            print("Fail to find the instance %s" % instance_id)
            return ""
        else:
            with open( ansible_hosts_file, "w" ) as fp:
                fp.write( "[dockers]\n")
                fp.write( "%s ansible_user=%s ansible_ssh_private_key_file=%s\n" % (inst['public_ip'], "root", self.config['key_pair_file']) )
            return ansible_hosts_file

    def ansible_playbook( self, instance_id, playbook_file ):
        for filename in playbook_file: self._ansible_playbook( instance_id, filename )

    def _ansible_playbook( self, instance_id, playbook_file ):
        """
        execute a ansible playbook on the instance. The playbook can be a local file or s3 file
        """
        ansible_hosts_file = self.create_ansible_hosts( instance_id )
        if ansible_hosts_file:
            if playbook_file.startswith( "s3://" ):
                filename = self._download_s3file( playbook_file )
            else:
                filename = playbook_file
            os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
            os.environ['ANSIBLE_INVENTORY'] = os.path.abspath(ansible_hosts_file)
            os.system( "ansible-playbook %s" % filename )
            if playbook_file.startswith( "s3://"):
                os.remove( filename )
                os.removedirs( os.path.dirname( filename ) )

class OpenStackEasyEC2( EasyEC2 ):
    NO_JSON_COMMANDS = [ ['server', 'delete'],
                         ['subnet', 'delete'],
                         ['router', 'add'],
                         ['router', 'set'],
                         ['router', 'delete'],
                         ['router', 'remove', 'subnet'],
                         ['server', 'add', 'floating', 'ip'],
                         ['server', 'remove', 'floating', 'ip'],
                         ['keypair', 'create'],
                         ['keypair', 'delete'],
                         ['floating', 'ip', 'delete'],
                         ['server', 'add', 'security', 'group'],
                         ['server', 'remove', 'security', 'group'],
                         ['security', 'group', 'delete'],
                         ['server', 'add', 'volume'],
                         ['server', 'remove', 'volume'],
                         ['volume', 'delete']
                    ]
                    
    def __init__( self, config ):
        self.config = config
        
    def _exec_command( self, cmd ):
        if not self._is_exec_file_exist( cmd[0] ):
            print( "executable file %s is not found,please install the python-openstackclient" % cmd[0] )
            return "executable file %s is not found" % cmd[0]
            
        if self._support_json_output( cmd ):
            cmd.append( '-f')
            cmd.append( 'json')
        if self._in_debug():
            print("start to execute command:%s" % (" ".join( cmd ) ))
        out = ""
        try:
            out = subprocess.check_output( cmd )
            if self._in_debug():
                print("Execute result:")
                print(out)
            return json.loads( out )
        except:
            return out 

    def _support_json_output( self, cmd ):
        for no_json_cmd in self.NO_JSON_COMMANDS:
            if len( no_json_cmd ) < len( cmd ) and no_json_cmd == cmd[1:len(no_json_cmd)+1]:
                return False
        return True
         
    def _in_debug( self ):
        return 'debug' in self.config and self.config['debug']        
    def list_images( self, image_id = "", os=""):
        images = self._exec_command( ['openstack', 'image', 'list', "--limit", "1000"])
        if image_id:
            for image in images:
                if image['ID'] == image_id:
                    return image
        if os:
            result = []
            for image in images:
                if image['Name'].find( os ) != -1:
                    result.append( image )
            return result
        else:
            return images
    def list_instance_types(self):
        return self._exec_command( ['openstack', 'flavor', 'list'])
        
    def start_instance( self, image_id, name, instance_type, tags = None, zone=None ):
        private_network = self.get_first_private_network()
        if not private_network:
            print( "Fail to find a private network, please create one")
            return {}
        if not instance_type:
            if 'default_instance_type' in self.config:
                instance_type = self.config['default_instance_type']
            else:
                instance_type = "m1.medium"
        image = self._find_image( image_id )
        if not zone:
            zone = self.get_first_available_zone()
        if image:
            cmd = ['openstack', 'server', 'create', 
                '--image', image['ID'], 
                '--flavor', instance_type, 
                '--key-name', self.config['key_pair'],
                '--nic', "net-id=%s"%private_network['name'],
                '--availability-zone', zone,
                name ]
            return self._exec_command(  cmd )
        else:
            print("Fail to find image %s" % image_id)

    def list_instances( self, name = "" ):
        instances = self._exec_command(  ['openstack', 'server', 'list'] )
        if not name:
            return instances

        result=[]

        if instances:
            for inst in instances:
                if inst['Name'] == name:
                    result.append( self._exec_command( ['openstack', 'server', 'show', inst['Name'] ] ) )
        return result
    def stop_instance( self, instance_id, force ):
        return self._exec_command(  ['openstack', 'server', 'stop', instance_id ] )
        
    def terminate_instance( self, instance_id ):
        return self._exec_command( ['openstack', 'server', 'delete', '--wait', instance_id ] )
        
    def find_instance( self, instance_id ):
        instances = self._exec_command(  ['openstack', 'server', 'list'] )
        if instances:
            for inst in instances:
                if instance_id == inst['ID'] or instance_id == inst['Name']:
                    return self._exec_command( ['openstack', 'server', 'show', inst['Name'] ] )
        print( "fail to find instance by name/id %s" % instance_id )
        return {}

    def create_tags( self, resource_id, tag ):
        return "Not support"
    def delete_tags( self, resource_id, tag):
        return "Not support"
    
    def create_volume( self, size, zone, name ):
        cmd =  ['openstack', 'volume', 'create', '--size', size ]
        if zone:
            cmd.append( '--availability-zone', zone )
        cmd.append( name )
        self._exec_command( cmd )
    def list_volumes( self, volume_id, status ):
        if volume_id:
            return self._exec_command( ['openstack', 'volume', 'show', volume_id ] )
        volumes = self._exec_command( ['openstack', 'volume', 'list'] ) 
        return volumes if status is None else [ volume for volume in volumes if volume['Status'] == status]

    def delete_volume( self, volume_id ):
        return self._exec_command( ['openstack', 'volume', 'delete', volume_id ] )

    def attach_volume( self, instance_id, volume_id, device ):
        if not device:
            device = '/dev/vdc'
        return self._exec_command( ['openstack', 'server', 'add', 'volume', '--device', device, instance_id, volume_id ] )
    def detach_volume( self, instance_id, volume_id, force ):
        return self._exec_command( ['openstack', 'server', 'remove', 'volume', instance_id, volume_id ] )
        
    def list_networks( self ):
        networks = self._exec_command( ['openstack', 'network', 'list'])
        result = []
        for network in networks:
            network_info = self._exec_command( ['openstack', 'network', 'show', network['Name'] ])
            if 'subnets' in network_info and network_info['subnets']:
                network_info['subnets'] = self._exec_command( ['openstack', 'subnet', 'show', network_info['subnets'] ])
            result.append( network_info )
        return result
    def create_network( self, name ):
        return self._exec_command( ['openstack', 'network', 'create', '--enable', '--internal', name ])
        
    def get_first_private_network( self ):
        networks = self.list_networks()
        if networks:
            for network in networks:
                if network['name'] != self.config['public_network'] and network['status'] == 'ACTIVE':
                    return network
        return {}
        
    def add_subnet( self, network_name, subnet_name, subnet_cidr ):
        cmd = ['openstack', 'subnet', 'create', '--network', network_name, '--subnet-range', subnet_cidr ]
        cmd.append( '--dhcp')
        if 'dns_servers' in self.config:
            for dns_server in self.config['dns_servers']:
                cmd.append( '--dns-nameserver')
                cmd.append( dns_server )
        cmd.append( subnet_name )
        
        self._exec_command( cmd )
        self._exec_command( ['openstack', 'router', 'create', "%s-gw" % subnet_name, '--enable'] )
        self._exec_command( ['openstack', 'router', 'add', 'subnet', "%s-gw" % subnet_name, subnet_name] )
        self._exec_command( ['openstack', 'router', 'set', "%s-gw" % subnet_name, '--external-gateway', self.config['public_network'] ])
        return "Success"
        
    def list_subnet( self, subnet_name ):
        if subnet_name:
            return self._exec_command( ['openstack', 'subnet', 'show', subnet_name ] )
        return self._exec_command( ['openstack', 'subnet', 'list' ] )      
    def remove_subnet( self, subnet_name ):
        self._exec_command( ['openstack', 'router', 'remove', 'subnet', '%s-gw' % subnet_name, subnet_name] )
        self._exec_command( ['openstack', 'router', 'delete', '%s-gw' % subnet_name] )
        return self._exec_command( ['openstack', 'subnet', 'delete', subnet_name ] )
        
    def create_router( self, name ):
        return self._exec_command( ['openstack', 'router', 'create', '--enable', name ] )

    def router_add_subnet( self, router_name, subnet_name ):
        return self._exec_command( ['openstack', 'router', 'add', 'subnet', router_name, subnet_name] )
        
    def list_routers( self ):
        routers = self._exec_command( ['openstack', 'router', 'list'] )
        result = []
        for router in routers:
            result.append( self.router_get_info( router['Name'] ) )
        return result
        
    def router_get_info( self, router_name ):
        router_info = self._exec_command( ['openstack', 'router', 'show', router_name] )
        if 'external_gateway_info' in router_info:
            try:
                gw_info = json.loads( router_info['external_gateway_info'] )
                router_info['external_gateway_info'] = gw_info
            except Exception as err:
                print( err )
        return router_info
        
    def elastic_ip_list( self, free = False ):
        all_ips = self._exec_command( ['openstack', 'floating', 'ip', 'list'])
        return [ ip for ip in all_ips if not ip['Port'] ] if free else all_ips
        
    def elastic_ip_attach( self, instance_id, ip_address ):
        return self._exec_command( ['openstack', 'server', 'add', 'floating', 'ip', instance_id, ip_address] )
    def elastic_ip_detach( self, instance_id, ip_address ):
        return self._exec_command( ['openstack', 'server', 'remove', 'floating', 'ip', instance_id, ip_address] )

    def elastic_ip_delete( self, ip_addr ):
        return self._exec_command( ['openstack', 'floating', 'ip', 'delete', ip_addr ])
    def create_elastic_ip( self ):
        return self._exec_command( ['openstack', 'floating', 'ip', 'create', self.config['public_network'] ] )
    def elastic_ip_alloc_attach( self, name ):
        print "instance name:%s" % name
	if not name:
            print "instance_id is not set"
        free_ips = self.elastic_ip_list( free = True )
        if free_ips:
            ip_info = {'floating_ip_address': free_ips[0]['Floating IP Address']}
        else:
            ip_info = self.create_elastic_ip()
	if ip_info and "floating_ip_address"  in ip_info:
            return self.elastic_ip_attach( name, ip_info["floating_ip_address"] )
        else:
            return "fail to allocate ip address"
    def ssh( self, instance_id, user = "root" ):
        if 'key_pair_file' not in self.config or len(self.config['key_pair_file']) <= 0:
            print( "no keypair file found under ~/.openstack directory")
            return
        ip_addr = self._get_elatic_ip_of( instance_id )
        if ip_addr:
            if user is None or len( user ) <= 0: user = "root"
            os.system( "ssh -i %s -o StrictHostKeyChecking=no %s@%s" %(self.config['key_pair_file'], user, ip_addr ) )
        else:
            print("Fail to find the VM by id or name:%s" % instance_id)

    def scp( self, from_file, to_file ):
        os.system( "scp -i %s -o StrictHostKeyChecking=no %s %s" % ( self.config['key_pair_file'], self._create_remote_file_info( from_file), self._create_remote_file_info( to_file ) ) )

    def _create_remote_file_info( self, remoteFile ):
        tmp = remoteFile.split( ":" )
        if len( tmp ) == 1:
            return tmp[0] 
        elif len( tmp ) == 2:
            return "root@%s:%s" % ( self._get_elatic_ip_of( tmp[0] ), tmp[1] )
        return ""
    def ansible_playbook( self, instance_id, playbook_file):
        for filename in playbook_file: self._ansible_playbook( instance_id, filename )

    def _ansible_playbook( self, instance_id, playbook_file):
        ansible_hosts_file = self.create_ansible_hosts( instance_id )
        if ansible_hosts_file:
            if playbook_file.startswith( "s3://" ):
                filename = self._download_s3file( playbook_file )
            else:
                filename = playbook_file
            os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
            os.environ['ANSIBLE_INVENTORY'] = os.path.abspath(ansible_hosts_file)
            os.system( "ansible-playbook %s" % filename )
            if playbook_file.startswith( "s3://"):
                os.remove( filename )
                os.removedirs( os.path.dirname( filename ) )

    def create_ansible_hosts( self, instance_id ):
        ip_addr = self._get_elatic_ip_of( instance_id )
        ansible_hosts_file = ".ansible_hosts"
        if not ip_addr:
            print("Fail to find the instance %s" % instance_id)
            return ""
        else:
            with open( ansible_hosts_file, "w" ) as fp:
                fp.write( "[dockers]\n")
                fp.write( "%s ansible_user=%s ansible_ssh_private_key_file=%s\n" % (ip_addr, "root", self.config['key_pair_file']) )
            return ansible_hosts_file
            
    def _get_elatic_ip_of( self, instance_id ):
        inst = self.find_instance( instance_id )
        if inst and 'addresses' in inst:
            addrs = inst['addresses']
            pos = addrs.rfind( '=' ) 
            if pos > 0:
                addrs = addrs[pos+1:]
            addrs = addrs.split(",")
            if len(addrs) == 1:
                return addrs[0].strip()
            for addr in reversed(addrs):
                addr = addr.strip()
                if len( addr ) > 0 and self._is_ip_reachable( addr ):
                    return addr
        return ""

    def _is_ip_reachable( self, ip ):
        try:
            subprocess.check_output( ['ping', '-c', '4', ip ] )
            return True
        except:
            return False
        
    def _find_image( self, image_id ):
        images = self.list_images()
        for image in images:
            if image['ID'] == image_id:
                return image
        for image in images:
            if image['Name'].find( image_id ) != -1:
                return image
        return None
        
    def create_keypair(self, name ):
        out = self._exec_command( ['openstack', 'keypair', 'create', name ])
	with open( '%s.pem' % name, 'wb' ) as fp:
		fp.write( out )

    def list_keypairs( self ):
        return self._exec_command( ['openstack', 'keypair', 'list'] )
    def delete_keypair( self, name ):
        return self._exec_command( ['openstack', 'keypair', 'delete', name ])
    def list_zones( self ):
        return self._exec_command( ['openstack', 'availability', 'zone', 'list' ])
    def get_first_available_zone( self ):
        zones = self.list_zones()
        for zone in zones:
            if zone['Zone Status'] == 'available':
                return zone['Zone Name']
        return ""
    def list_sec_group( self ):
        sec_groups = self._exec_command(['openstack', 'security', 'group', 'list'])
        result = []
        for group in sec_groups:
            result.append( self._exec_command(['openstack', 'security', 'group', 'show', group['Name'] ] ) )
        return result
        
    def create_sec_group( self, group_name, desc):
        cmd = ['openstack', 'security', 'group', 'create']
        if desc:
            cmd.append( '--description')
            cmd.append( desc )
        cmd.append( group_name )
        return self._exec_command( cmd )
    def delete_sec_group( self, group_name ):
        cmd = ['openstack', 'security', 'group', 'delete', group_name]
        return self._exec_command( cmd )
        
    def add_sec_group_ingress_rule( self, group_name, protocol, port_range ):
        return self._exec_command( ['openstack', 'security', 'group', 'rule', 'create', '--protocol', protocol, '--dst-port', port_range, '--src-ip', '0.0.0.0/0', '--ingress', group_name] )
        
    def add_sec_group_egress_rule( self, group_name, protocol, port_range ):
        return self._exec_command( ['openstack', 'security', 'group', 'rule', 'create', '--protocol', protocol, '--dst-port', port_range, '--src-ip', '0.0.0.0/0', '--egress', group_name] )
        
    def attach_sec_group( self, group_name, instance_id ):
        return self._exec_command( ['openstack', 'server', 'add', 'security', 'group', instance_id, group_name ] )  

    def detach_sec_group( self, group_name, instance_id ):
        return self._exec_command( ['openstack', 'server', 'remove', 'security', 'group', instance_id, group_name ] )

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
                ip_addr = self._get_elatic_ip_of( host )
                if ip_addr:
                    os.system( "ssh -i %s root@%s s3cmd get %s %s" % ( self.config['key_pair_file'], ip_addr, from_file, to_file[to_file.find( ':' ) + 1:] ) )
                else:
                    print("no host %s is found" % host)
            else: # copy the s3 file to local
                os.system( "s3cmd get %s %s" % (from_file, to_file) )
        elif to_file.startswith( "s3://"):
            if from_file.find( ':' ) != -1: #try to put remote file to s3
                host = from_file[0:from_file.find( ':') ]
                ip_addr = self._get_elatic_ip_of( host )
                if ip_addr:
                    os.system( "ssh -i %s root@%s s3cmd put %s %s" % ( self.config['key_pair_file'], ip_addr, from_file[from_file.find( ':' ) + 1: ], to_file ) )
            else: # try to put local to s3
                os.system( "s3cmd put %s %s" % ( from_file, to_file) )    
    def version( self ):
        version_info = subprocess.check_output(['openstack', '--version'], stderr=subprocess.STDOUT )
        words = version_info.strip().split()
        return words[1] if len(words) > 1 else words[0]
def printAsJson( o ):
    if not o:
        return
    try:
        print( json.dumps( o, indent = 4 ) )
    except:
        print(o)

class EasyEC2ConfigLoader:
    def load_config( args ):
        return {}
    def _find_file_with_suffix_in_directory( self, dirName, suffix ):
        result = []
        if os.path.isdir( dirName ):
            files = os.listdir( dirName )
            for f in files:
                if os.path.isfile( dirName + '/' + f ) and f.endswith( suffix ):
                    result.append( dirName + '/' + f )
        return result
    def _find_key_pair( self, key_pair_file ):
        if key_pair_file:
            return os.path.basename( key_pair_file )[:-4]
        return ""
    def _set_debug_flag( self, args, config ):
        if config:
            if '--debug' in args and args['--debug']:
                config['debug'] = True
            elif '-d' in args and args['-d']:
                config['debug'] = True
            else:
                config['debug'] = False

class EucaConfigLoader( EasyEC2ConfigLoader ):
    def __init__( self, args ):
        self.args = args
        if '--config_dir' in args and args['--config_dir']:
            self.config_dir = os.path.expanduser( args['--config_dir'] )
        else:
            self.config_dir = os.path.expanduser('~/.euca' )
        
    def load_config( self ):
        euca_config = self._load_euca_ini( self._find_euca_ini() )
        key_pair_file = self._find_key_pair_file()
        config = {}
        if key_pair_file and euca_config:
            config['access_id'] = self._get_from_euca_config( euca_config, 'key-id' )
            config['access_key'] = self._get_from_euca_config( euca_config, 'secret-key' )
            config['key_pair'] = self._find_key_pair( key_pair_file )
            config['key_pair_file'] = key_pair_file
            self._set_debug_flag( self.args, config )
        return config
            
    def _load_euca_ini( self, eucaIniFile ):
        if eucaIniFile:
            config = ConfigParser.ConfigParser()
            config.read( [eucaIniFile] )
            return config
        return {}
    
    def _get_from_euca_config( self, euca_config, key ):
        for section in euca_config.sections():
            for item in euca_config.items( section ):
                if item[0] == key:
                    return item[1]
        return ""
    
    
    def _find_euca_ini( self ):
        files = self._find_file_with_suffix_in_directory( self.config_dir, "euca2ools.ini")
        if files:
            return files[0]
        return ""
    
    
    def _find_key_pair_file( self ):
        files = self._find_file_with_suffix_in_directory( self.config_dir, ".pem")
        for f in files:
            name = os.path.basename( f )
            if (name.endswith( ".pem" ) and 
                    not name.startswith( "euca2-" ) and 
                    not name.endswith( "cert.pem") and
                    not name.endswith( "pk.pem" ) ):
                return f
        return ""    
    
class OpenStackConfigLoader( EasyEC2ConfigLoader ):
    def __init__( self, args ):
        self.args = args
        if '--config_dir' in args and args['--config_dir']:
            self.config_dir = os.path.expanduser( args['--config_dir'] )
        else:
            self.config_dir = os.path.expanduser('~/.openstack' )
        
    def load_config( self ):
        '''
        load the openstack configuration from openstack.ini file
        '''
        
        ini_file = self._find_openstack_ini_file()
        print "load configuration from file %s" % ini_file
        key_pair_file = self._find_key_pair_file()
        if ini_file:
            ini_config = self._load_openstack_ini_file( ini_file )
            if ini_config:
                for item in ini_config.items( 'AUTH'):
                    key = item[0].upper().strip()
                    val = item[1].strip()
                    if val.startswith( '"' ) and val.endswith( '"'):
                        val = val[1:-1]
                    os.environ[ key ] = val
                config = {}
                if ini_config.has_option( 'DEFAULT', 'public_network'):
                    config['public_network'] = ini_config.get( 'DEFAULT', 'public_network')
                if ini_config.has_option( 'DEFAULT', 'dns_servers'):
                    config['dns_servers'] = []
                    for server in ini_config.get( 'DEFAULT', 'dns_servers').split( ','):
                        server = server.strip()
                        if server:
                            config['dns_servers'].append( server )
                if ini_config.has_option( 'DEFAULT', 'default_instance_type'):
                    config['default_instance_type'] = ini_config.get( 'DEFAULT', 'default_instance_type' )
                config['key_pair_file'] = key_pair_file
                if key_pair_file:
                    config['key_pair'] = self._find_key_pair( key_pair_file )
                self._set_debug_flag( self.args, config )
                return config
                
        return {}

    def _load_openstack_ini_file( self, fileName ):
        try:
            config = ConfigParser.ConfigParser()
            config.read( [fileName])
            return config
        except:
            return {}
                    
    def _find_openstack_ini_file( self ):
        ini_file = "%s/openstack.ini" % self.config_dir 
        if os.path.isfile( ini_file ):
            return ini_file
        else:
            return ""
            
    def _find_key_pair_file( self ):
        files = self._find_file_with_suffix_in_directory( self.config_dir, ".pem")
        if files:
            return files[0]
        else:
            return ""    
def createEasyEC2( args ):
    def createEuca( config ):
        return EucaEasyEC2( config )
    def createOpenStack( config ):
        return OpenStackEasyEC2( config )
   
    clouds = [{'config_loader': EucaConfigLoader( args ), 'creator': createEuca },
              {'config_loader': OpenStackConfigLoader( args ), 'creator': createOpenStack} ]
    for cloud in clouds:
        config = cloud['config_loader'].load_config()
        if config:
            return cloud['creator']( config )            
    return EasyEC2()

class FunctionDispatcher:
    def __init__( self, easy_ec2 ):
        self.easy_ec2 = easy_ec2
        self.methods = [['ansible', 'playbook', '<instance_id>', '<playbook_file>', easy_ec2.ansible_playbook ],
                        ['image', "list", "--id", "--os", easy_ec2.list_images ],
                        ["instance", "list", "--name", easy_ec2.list_instances],
                        ["instance", "start", "<image_id>", "<name>", "--type", "--zone", easy_ec2.start_instance ], 
                        ["instance", "terminate", "<instance_id>",  easy_ec2.terminate_instance ],
                        ["instance", "stop", '<instance_id>', '--force', easy_ec2.stop_instance ],
                        ['instance', 'types', easy_ec2.list_instance_types ],
                        ['ip', 'list', "--free", easy_ec2.elastic_ip_list ],
                        ['ip', 'alloc', easy_ec2.create_elastic_ip ],
                        ['ip', 'alloc-attach', "<instance_id>", easy_ec2.elastic_ip_alloc_attach],
                        ['ip', 'delete', '<ip_addr>', easy_ec2.elastic_ip_delete ],
                        ['ip', 'attach', '<instance_id>', '<elastic_ip>', easy_ec2.elastic_ip_attach],
                        ['ip', 'detach', '<instance_id>', '<elastic_ip>', easy_ec2.elastic_ip_detach],
                        ['keypair', 'create', '<name>', easy_ec2.create_keypair],
                        ['keypair', 'delete', '<name>', easy_ec2.delete_keypair ],
                        ['keypair', 'list', easy_ec2.list_keypairs ],
                        ['network', 'list', easy_ec2.list_networks ],
                        ['network', 'create', '<network_name>', easy_ec2.create_network],
                        ['sec-group', 'list', easy_ec2.list_sec_group],
                        ['sec-group', 'create', '<group_name>', '--description', easy_ec2.create_sec_group],
                        ['sec-group', 'delete', '<group_name>', easy_ec2.delete_sec_group],
                        ['sec-group', 'ingress', '<group_name>', '<protocol>', '<port_range>', easy_ec2.add_sec_group_ingress_rule],
                        ['sec-group', 'egress', '<group_name>', '<protocol>', '<port_range>', easy_ec2.add_sec_group_egress_rule],
                        ['sec-group', 'attach', '<group_name>', '<instance_id>', easy_ec2.attach_sec_group],
                        ['sec-group', 'detach', '<group_name>', '<instance_id>', easy_ec2.detach_sec_group],
                        ['ssh', '<name>', "--user", easy_ec2.ssh ],
                        ['scp', '<from_file>', '<to_file>', easy_ec2.scp ],
                        ['subnet', 'add', '<network_name>', '<subnet_name>', '<subnet_cidr>', easy_ec2.add_subnet ],
                        ['subnet', 'list', '--name', easy_ec2.list_subnet ],
                        ['subnet', 'remove', '<subnet_name>', easy_ec2.remove_subnet ],
                        ['s3', 'cp', '<from_file>', '<to_file>', easy_ec2.s3_copy ],
                        ['s3', 'share', '<s3_bucket_file>', easy_ec2.s3_share ],
                        ['s3', 'ls', '<bucket>', easy_ec2.s3_ls ],
                        ['tags', 'create', '<resource_id>', '<tag>', easy_ec2.create_tags ],
                        ['tags', 'delete', '<resource_id>', '<tag>', easy_ec2.delete_tags ],
                        ['volume', 'list', '--id', "--status", easy_ec2.list_volumes ],
                        ['volume', 'create', '<size>', '--zone', '--name', easy_ec2.create_volume ],
                        ['volume', 'delete', '<volume_id>', easy_ec2.delete_volume ],
                        ['volume', 'attach', '<instance_id>', '<volume_id>', '--device', easy_ec2.attach_volume ],
                        ['volume', 'detach', '<instance_id>', '<volume_id>', '--force', easy_ec2.detach_volume ],
                        ['zone', 'list', easy_ec2.list_zones ],
                        ['version', easy_ec2.version]
                    ]
                            
    def dispatch( self, args ):
        for method in self.methods:
            i = 0
            n = len( method ) - 1
            params = []
            while i < n:
                if method[i].startswith( '--') or method[i].startswith( '<' ):
                    params.append( args[method[i] ] )
                elif not args[method[i]]:
                    break
                i += 1
            if i == n:
                printAsJson( method[-1](*params) )
                break

def main():
    args = docopt.docopt( __doc__, version="1.0" )
    easy_ec2 = createEasyEC2( args )
    dispatcher = FunctionDispatcher( easy_ec2 )
    dispatcher.dispatch( args )

if __name__ == "__main__":
    main()

