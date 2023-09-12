import subprocess
interface = input("pleace select interface :" )
mac = input("slect ypur mac address :")

subprocess.run("ifconfig " + interface + " down" , shell=True )
subprocess.run("ifconfig " + interface  +" hw ether " + mac , shell=True )
subprocess.run("ifconfig " + interface  + " up" , shell=True )

print("mac address changed successfully")