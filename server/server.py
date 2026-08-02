import time

wiredConnections = ["Manager's Office Computer - IP: 192.168.1.10","Manager's Office landline - IP: 192.168.1.11",
                    "Human Resources Computer - IP: 192.168.1.12","Human Resources landline - IP: 192.168.1.13",]

wirelessConnections = ["Iphone","Samsung3s","Blackberry","Samsung Z-fold","Verizon chocolate",
                       "Dell XPS","Macbook Pro", "Boost Mobile Side-kick",]

IPAddresses = ["192.168.1.10","192.168.1.11","192.168.1.12","192.168.1.13"]

deviceSerialNumbers = ["SN-001","SN-002","SN-003","SN-004","SN-005","SN-006","SN-007",]

devices = ["router","switch","PC1","PC2","VOIP Phone","Wireless Access Point","server",]

class firewall():
        def firewallConnection(self): 
            print(' 🤖 Running firewall diagnostic...') 
            time.sleep(6)
            
            print(" 🧯Incoming malicious traffic detected, blocking traffic...")
            time.sleep(9)
            
            print(" 🛡️ Malilious traffic blocked. Incoming/outgoing traffic clear ")
            time.sleep(3)            
            
            print(" Firewall - SAFE \n")
            

class router():
        def routerConnection(self):
            print("Router loading...")
            time.sleep(.5)
            
            print(" ✅ Connected\n")

class server():
        def ServerConection(self):
            print("Server loading...")
            time.sleep(.7)
            
            print(" ✅ Connected\n")

class switch():
        def switchConection(self):            
            print("Switch loading...")
            time.sleep(.7)
            
            print(" ✅ Connected\n")
            time.sleep(.7)
            
            print("Devices connected to the switch:")
            
            for device in wiredConnections:
                print(device)
            print(" 📞 Total Wired Connections: " + str(len(wiredConnections)) + "\n")

class WAP():
        def wapConnection(self):
            print("WAP loading...")
            time.sleep(.7)
            
            print("Connected\n")         
        
            for device in wirelessConnections:
                print(device)
            print(" 💻 Total Wireless Connections:  " + str(len(wirelessConnections)) + "\n")       
