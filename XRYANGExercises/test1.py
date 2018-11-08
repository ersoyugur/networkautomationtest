from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper as xr_shellutil_oper
from datetime import timedelta

if __name__ == "__main__":
    """Main execution path"""
    
    # create NETCONF session
    provider = NetconfServiceProvider(address="200.200.200.200",
                                      port=830,
                                      username="ugur",
                                      password="ugur19",
                                      protocol="ssh")
    # create CRUD service
    crud = CRUDService()
    
    # create system time object
    system_time = xr_shellutil_oper.SystemTime()
   
    # read system time from device
    system_time = crud.read(provider, system_time)
    
    # Print system time
    print("System uptime is " +  
          str(system_time.uptime.uptime))
    
    # close NETCONFIG session and exit
    provider.close()
    exit()  
