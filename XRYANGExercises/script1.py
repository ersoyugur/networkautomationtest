#!/usr/bin/env python
from ydk.services import  NetconfService,Datastore
from ydk.providers import NetconfServiceProvider
from ydk.models.openconfig import openconfig_bgp as oc_bgp
from ydk.models.openconfig import openconfig_bgp_types as oc_bgp_types
import time

username = 'ugur'
password = 'ugur19'
netconf_port = 830
iosxr_host = '200.200.200.200'
junos_host = 'https://www.linkedin.com/redir/invalid-link-page?url=172%2e16%2e0%2e12'

# Function used to generate the BGP configuration
def config_bgp(bgp,global_as,router_id,peer_group_name,remote_as,remote_peer):
    
"""Add config data to bgp object."""
    # global configuration
    bgp.global_.config.as_ = global_as
    bgp.global_.config.router_id = router_id
    afi_safi = bgp.global_.afi_safis.AfiSafi()
    afi_safi.afi_safi_name = oc_bgp_types.Ipv4UnicastIdentity()
    afi_safi.config.enabled = True
    bgp.global_.afi_safis.afi_safi.append(afi_safi)
    afi_safi.config.enabled = True
    # configure IBGP peer group
    peer_group = bgp.peer_groups.PeerGroup()
    peer_group.peer_group_name = peer_group_name
    peer_group.config.peer_group_name = peer_group_name
    peer_group.config.peer_as = remote_as
    afi_safi = peer_group.afi_safis.AfiSafi()
    afi_safi.afi_safi_name = oc_bgp_types.Ipv4UnicastIdentity()
    afi_safi.config.enabled = True
    peer_group.afi_safis.afi_safi.append(afi_safi)
    bgp.peer_groups.peer_group.append(peer_group)
    # configure IBGP neighbor
    neighbor = bgp.neighbors.Neighbor()
    neighbor.neighbor_address = remote_peer
    neighbor.config.neighbor_address = remote_peer
    neighbor.config.peer_group = peer_group_name
    bgp.neighbors.neighbor.append(neighbor)

if __name__ == "__main__":
    """Execute main program."""
    # create IOS-XR NETCONF provider
    xr_provider = NetconfServiceProvider(address=iosxr_host,
                                         port=netconf_port,
                                         username=username,
                                         password=password,
                                         timeout=10)
    # create JunOS NETCONF provider
    ##junos_provider = NetconfServiceProvider(address=junos_host,
    ##                                        port=netconf_port,
    ##                                        username=username,
    ##                                        password=password,
    ##                                        timeout=10)

    #create an instance of the netconf service
    netconf = NetconfService()

    # Create an IOSXR instance from the OpenConfig BGP Model
    xr_bgp = oc_bgp.Bgp()
    # Create an JunOS instance from the OpenConfig BGP Model
    #junos_bgp = oc_bgp.Bgp()
    # Populate the BGP object with xr Configuration
config_bgp(xr_bgp,global_as=100,router_id='1.1.1.1',peer_group_name='EBGP',remote_as=101,remote_peer='1.1.1.1')
    # Populate the BGP object with JunOS Configuration
#config_bgp(junos_bgp,global_as=101,router_id='https://www.linkedin.com/redir/invalid-link-page?url=10%2e1%2e3%2e2',peer_group_name='EBGP',remote_as=100,remote_peer='https://www.linkedin.com/redir/invalid-link-page?url=10%2e1%2e3%2e1')

    # Send the XR bgp object via NETCONF to the Candidate DataStore on the XR router
    netconf.edit_config(xr_provider,Datastore.candidate,xr_bgp)
    # commit the configuration
    netconf.commit(xr_provider)
    # close the NETCONF session towards the XR router
    xr_provider.close()
    # Wait for 2 second
    time.sleep(2)
    # Send the JUnOS bgp object via NETCONF to the Candidate DataStore on the JUnOS router
    netconf.edit_config(junos_provider,Datastore.candidate,junos_bgp)
    # commit the configuration
    netconf.commit(junos_provider)
    # close the NETCONF session towards the JUnOS router
    #junos_provider.close()
    exit()  
