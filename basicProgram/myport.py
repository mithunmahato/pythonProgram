report_name = "Catalyst Center managed devices"
column_titles = ["Name", "Platform","Management IP","SW/FW version"]
print(f"***My Report : {report_name}***")
print(column_titles) 

network_devices = [
  {
    "hostname" : "rtr1",
    "family" : "Routers",
    "platform": "C8200L-1N-4T",
    "mgmt_ip":"10.10.20.174",
    "version":"17.9.20220318:182713"
  },
  {

    "hostname" : "sw1",
    "family" : "Switches and Hubs",
    "platform": "C9KV-UADP-8P",
    "mgmt_ip":"10.10.20.175",
    "version":"17.9.20220318:182713"
  },
  {
    "hostname" : "sw2",
    "family" : "Switches and Hubs",
    "platform": "C9KV-UADP-8P",
    "mgmt_ip":"10.10.20.176",
    "version":"17.9.20220318:182713"
  }
]
"""
print(network_devices)
print(f"{network_devices[0]['hostname']}, {network_devices[0]['platform']}, {network_devices[0]['mgmt_ip']}, {network_devices[0]['version']}")
print(f"{network_devices[1]['hostname']}, {network_devices[1]['platform']}, {network_devices[1]['mgmt_ip']}, {network_devices[1]['version']}")
print(f"{network_devices[2]['hostname']}, {network_devices[2]['platform']}, {network_devices[2]['mgmt_ip']}, {network_devices[2]['version']}")
"""

for device in network_devices:
  print(f"{device['hostname']},{device['platform']},{device['mgmt_ip']},{device['version']}")