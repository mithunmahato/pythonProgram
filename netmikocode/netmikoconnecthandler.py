#!/usr/bin/python3

from netmiko import ConnectHandler
import os

ciscoDevice = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.10',
    'username': 'cisco',
    'password': 'cisco',
}
with ConnectHandler(**ciscoDevice) as c:
        r1=c.send_command("sh ip int bri")
        r2=c.send_command("sh run")
        print(r1)
        print(r2)

"""#Normal Execution
c = ConnectHandler(**ciscoDevice) # use of kwargs optional, could just use regular parameters
r1 = c.send_command("sh ip int bri")
print(r1)
r2=c.send_command("sh run")
print(r2)
c.disconnect() # To disconnect the device
#With Conext manager and save the file
with open('output.txt','w') as a:
    sys.stdout=a
    with ConnectHandler(**ciscoDevice) as c:
        r1=c.send_command("sh ip int bri")
        r2=c.send_command("sh cdp nei")
        print(r1)
        print(r2)

#python3 netmikoconnecthandler.py | tee config.txt to save directly to a text file
"""
