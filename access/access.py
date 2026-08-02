import time
import secrets

class userAccess():
    def randomBool(self):
        return bool(secrets.randbelow(2))
    
    def biometric(self):
        print(" Place your thumb on the reader...")
        time.sleep(3)
        
        print(" 🫆 Scanning identity")
        time.sleep(3)
        
        while True: 
            fingerprint = self.randomBool()
            
            if fingerprint is False:
                print(" 🛑 Access denied")
                return False   

            else:
                time.sleep(3)
                print(" 🆗 Access granted")
                return True    
