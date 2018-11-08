#!/usr/bin/env python
from ydk.services import CRUDService		
from ydk.providers import NetconfServiceProvider		
from ydk.models.openconfig import openconfig_bgp as oc_bgp
if __name__ == "__main__":		
	provider = NetconfServiceProvider(address="200.200.200.200", port=830, username='ugur', password='ugur19', protocol='ssh')		
	crud = CRUDService()	 #	create	CRUD	service	
	bgp = oc_bgp.Bgp()		#	create	oc-bgp	object		
	bgp.global_.config.as_	= 65000		#	set	local	AS	number		
	crud.create(provider, bgp)		#	create	on	NETCONF	device	
	provider.close()	
	exit()	
