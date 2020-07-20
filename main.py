import subprocess
import socket

host_name = socket.gethostname()
ipaddr = socket.gethostbyname(host_name)

numbers = ipaddr.split(".")
ip_template = ""

for i in range(3):
    ip_template += numbers[i] + "."

locations = 255
for i in range(locations):
    newaddr = ip_template + str(i)
    response = subprocess.call(['ping','-c','3',newaddr])