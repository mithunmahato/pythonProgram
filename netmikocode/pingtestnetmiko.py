from netmiko import ConnectHandler
import getpass

device={
    'device_type': 'cisco_ios',
    'host':   '198.18.134.10',
    'username':input('Enter username : '),
    'password': getpass.getpass()
}
c=ConnectHandler(**device)
print('Device got connected')
output=c.send_command("sh ip int bri")
print(output)