from ncclient import manager
import xmltodict
import xml.dom.minidom


netconf_filter = """
 
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface></interface>
   </interface>
 </filter>

		"""

with  manager.connect(
   #host=env_lab.IOS_XE_1["host "],
   host="ios-xe-mgmt.cisco.com",
   port="10000",
   #port=env_lab.IOS_XE_1["netconf_port"],
   username="root",
   password="D_Vay!_10&",
   #username=env_lab.IOS_XE_1["username"],
   #password=env_lab.IOS_XE_1["password"],
   hostkey_verify=False
   ) as m:

#for capability in m.server_capabilities:
#   print(capability)
	netconf_fullconfig = m.get_config(source = 'running')
	print(xml.dom.minidom.parseString(netconf_fullconfig.xml).toprettyxml()) ## Print raw XML in pretty fashion
	print ("==========================")
	netconf_reply = m.get_config(source = 'running', filter = netconf_filter)
	#print netconf_reply  Really unreadable
	print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) ## Print raw XML in pretty fashion
	print ("==========================")
# Parse the returned XML to an Ordered Dictionary
	netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
	interfaces = netconf_data["interfaces"]["interface"]
	for interface in interfaces:
     		print("Interface {} enabled status is {}".format(interface["name"], interface["enabled"])
             	
         )



#m.close_session()
exit()
