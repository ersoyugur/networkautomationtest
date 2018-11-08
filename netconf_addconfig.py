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

m =  manager.connect(
   #host=env_lab.IOS_XE_1["host "],
   host="ios-xe-mgmt.cisco.com",
   port="10000",
   #port=env_lab.IOS_XE_1["netconf_port"],
   username="root",
   password="D_Vay!_10&",
   #username=env_lab.IOS_XE_1["username"],
   #password=env_lab.IOS_XE_1["password"],
   hostkey_verify=False
   )

#for capability in m.server_capabilities:
#   print(capability)
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
	    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                 {type}
            </type>
            <enabled>{status}</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>"""


netconf_data = netconf_interface_template.format(
        name = "Loopback700",
        desc = "KaracalTestInterface",
        type =  "ianaift:softwareLoopback",
        status = "false",
        ip_address = "70.70.70.70",
        mask = "255.255.255.255"
    )

netconf_reply = m.edit_config(netconf_data, target = 'running')


#m.close_session()
exit()
