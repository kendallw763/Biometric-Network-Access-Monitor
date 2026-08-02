from time import time
from server.server import firewall, router, server, switch, WAP
from access.access import userAccess
import sys

def main():
    userAccess_obj = userAccess()
    firewall_obj = firewall()
    router_obj = router()
    server_obj = server()
    switch_obj = switch()
    wap_obj = WAP()

    if userAccess_obj.biometric() is False:
        print("You are not authorized...")
        sys.exit()
        
    firewall_obj.firewallConnection()
    router_obj.routerConnection()
    server_obj.ServerConection()
    switch_obj.switchConection()
    wap_obj.wapConnection()
  
if __name__ == '__main__':
    main()
