import time
#=======================#=======================#=======================#=======================
wiredConnections = [
    "Manager's Office Computer - IP: 192.168.1.10 - SN: SN-008",
    "Manager's Office landline - IP: 192.168.1.11 - SN: SN-009",
    "Human Resources Computer - IP: 192.168.1.12 - SN: SN-010",
    "Human Resources landline - IP: 192.168.1.13 - SN: SN-011",
]

wirelessConnections = [
    "Iphone - IP: 192.168.1.20 - SN: SN-012",
    "Samsung3s - IP: 192.168.1.21 - SN: SN-013",
    "Blackberry - IP: 192.168.1.22 - SN: SN-014",
    "Samsung Z-fold - IP: 192.168.1.23 - SN: SN-015",
    "Verizon chocolate - IP: 192.168.1.24 - SN: SN-016",
    "Dell XPS - IP: 192.168.1.25 - SN: SN-017",
    "Macbook Pro - IP: 192.168.1.26 - SN: SN-018",
    "Boost Mobile Side-kick - IP: 192.168.1.27 - SN: SN-019",
]

IPAddresses = [
    "192.168.1.10","192.168.1.11","192.168.1.12","192.168.1.13",
    "192.168.1.20","192.168.1.21","192.168.1.22","192.168.1.23",
    "192.168.1.24","192.168.1.25","192.168.1.26","192.168.1.27",
    "192.168.1.30","192.168.1.31","192.168.1.32","192.168.1.33",
    "192.168.1.34","192.168.1.35","192.168.1.36"
]


deviceSerialNumbers = [
    "SN-001","SN-002","SN-003","SN-004","SN-005","SN-006","SN-007",
    "SN-008","SN-009","SN-010","SN-011","SN-012","SN-013","SN-014",
    "SN-015","SN-016","SN-017","SN-018","SN-019"
]

devices = [
    # Core network devices (7)
    "Router - IP: 192.168.1.30 - SN: SN-001",
    "Switch - IP: 192.168.1.31 - SN: SN-002",
    "PC1 - IP: 192.168.1.32 - SN: SN-003",
    "PC2 - IP: 192.168.1.33 - SN: SN-004",
    "VOIP Phone - IP: 192.168.1.34 - SN: SN-005",
    "Wireless Access Point - IP: 192.168.1.35 - SN: SN-006",
    "server - IP: 192.168.1.36 - SN: SN-007",

    # Wired devices (4)
    "Manager's Office Computer - IP: 192.168.1.10 - SN: SN-008",
    "Manager's Office Landline - IP: 192.168.1.11 - SN: SN-009",
    "HR Computer - IP: 192.168.1.12 - SN: SN-010",
    "HR Landline - IP: 192.168.1.13 - SN: SN-011",

    # Wireless devices (8)
    "Iphone - IP: 192.168.1.20 - SN: SN-012",
    "Samsung3s - IP: 192.168.1.21 - SN: SN-013",
    "Blackberry - IP: 192.168.1.22 - SN: SN-014",
    "Samsung Z-fold - IP: 192.168.1.23 - SN: SN-015",
    "Verizon chocolate - IP: 192.168.1.24 - SN: SN-016",
    "Dell XPS - IP: 192.168.1.25 - SN: SN-017",
    "Macbook Pro - IP: 192.168.1.26 - SN: SN-018",
    "Boost Mobile Side-kick - IP: 192.168.1.27 - SN: SN-019",
]
#=======================#=======================#=======================#=======================
class firewall():
        def firewallConnection(self): 
            print(' 🤖 Running firewall diagnostic...') 
            time.sleep(6)
            
            print(" 🧯Incoming malicious traffic detected, blocking traffic...")
            time.sleep(9)
            
            print(" 🛡️ Malilious traffic blocked. Incoming/outgoing traffic clear ")
            time.sleep(3)            
            
            print(" Firewall - SAFE \n")
#=======================#=======================#=======================#=======================
class router():
        def routerConnection(self):
            print("Router loading...")
            time.sleep(.5)
            
            print(" ✅ Connected\n")
#=======================#=======================#=======================#=======================
class server():
        def ServerConection(self):
            print("Server loading...")
            time.sleep(.7)
            
            print(" ✅ Connected\n")
#=======================#=======================#=======================#=======================
class switch():
        def switchConection(self):            
            print("Switch loading...")
            time.sleep(.7)
            
            print(" ✅ Connected\n")
            time.sleep(.7)
            
            print("SWITCH CONNECTIONS: ")
            
            for device in wiredConnections:
                print(device)
            print(" 📞 WIRELESS CONNECTIONS: " + str(len(wiredConnections)) + "\n")
#=======================#=======================#=======================#=======================
class WAP():
        def wapConnection(self):
            print("WAP loading...")
            time.sleep(.7)
            
            print(" ✅ Connected\n")    
            
            print("WAP CONNECTIONS: ")     
        
            for device in wirelessConnections:
                print(device)
            print(" 💻 WIRELESS CONNECTIONS:  " + str(len(wirelessConnections)) + "\n")       
            
class DeviceCount():
    def deviceCount(self):
        print("TOTAL NETWORK CONNECTIONS: ")
        for device in devices:
            print( device + "\n")
