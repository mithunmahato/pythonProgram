from netmiko import ConnectHandler
import os
import csv
from datetime import date,time
from dotenv import load_dotenv

load_dotenv('.envrc')

def main():
    #read device info from csv file
    with open('device_info.csv','r') as device_info:
        reader=csv.DictReader(device_info)
        #receive credential from enviroment variable
        for device in reader:
            username=os.getenv('USERNAME')
            password=os.getenv('PASSWORD')
            takebackup(device,username,password)

def takebackup(device,username,password):
    device_connect=ConnectHandler(
        ip=device['ip_address'],
        username=username,
        password=password,
        device_type=device['device_type']
    )


