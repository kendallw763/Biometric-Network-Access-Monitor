from server.server import firewall, router, server, switch, WAP, DeviceCount
from access.access import Credentials, BiometricScan
global fingerprint
#=======================#=======================#=======================#=======================
def main():
    credentials_obj = Credentials()
    biometricScan_obj = BiometricScan()
    firewall_obj = firewall()
    router_obj = router()
    server_obj = server()
    switch_obj = switch()
    wap_obj = WAP()
    deviceCount_obj = DeviceCount()
    credentials_obj.userPassCredentials()
    biometricScan_obj.biometric()
    firewall_obj.firewallConnection()
    router_obj.routerConnection()
    server_obj.serverConnection()
    switch_obj.switchConnection()
    wap_obj.wapConnection()
    deviceCount_obj.deviceCount()

if __name__ == '__main__':
    main()
    #unittest.main()