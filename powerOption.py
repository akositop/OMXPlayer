import os

class powerOptions():
    def shutdown(obj):
        os.system("sudo shutdown -h now")
        print ("posys\n")
    def restart(obj):
        os.system("sudo shutdown -r now")
        print ("posys\n")
    
