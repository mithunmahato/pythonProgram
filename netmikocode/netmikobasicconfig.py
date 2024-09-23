from netmiko import ConnectHandler
import os


devices = {
    'device_type': 'cisco_ios',
    'host':   '198.18.134.10',
    'username': "cisco",
    'password': "cisco"
    }

commands = [
    "int loopback0",
    "ip add 10.10.10.10 255.255.255.0",
    "description Configured by Netmiko",
]

with ConnectHandler(**devices) as connection:
    output = connection.send_config_set(commands)
    connection.save_config()
    print(output)