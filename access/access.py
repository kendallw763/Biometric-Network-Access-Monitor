import time
import getpass
#=======================#=======================#=======================#=======================
names = [
    "name1",
    "name2",
    "name3",
    "name4",
    "name5"
]

credentials = [
    "str1",
    "str2",
    "str3",
    "str4",
    "str5"
]

fingerPrint = True
#=======================#=======================#=======================#=======================
class Credentials:
    @staticmethod
    def userPassCredentials():
        while True:
            print("=== Welcome ===")
            username = input("Enter your name: ").strip()
            print("")
            
            password = getpass.getpass("Enter your password: ")
            print("")

            if username not in names:
                print("Access denied — user not found.\n")
                continue

            if password not in credentials:
                print("Access denied — password not found.\n")
                continue

            user_index = names.index(username)
            password_index = credentials.index(password)

            if user_index != password_index:
                print("Access denied — name/password mismatch.\n")
                continue

            print(f"Welcome {username}!\n")
            time.sleep(3)
            print("Place your thumb on the reader...")
            time.sleep(3)
           
            return True 
#=======================#=======================#=======================#=======================
class BiometricScan:
    @staticmethod
    def biometric():
        print(" 🫆 Scanning fingerprint...")
        time.sleep(3)

        if not fingerPrint:
            print(" 🛑 Access denied")
            return False
        else:
            print(" 🆗 Access granted")
            return True


        

