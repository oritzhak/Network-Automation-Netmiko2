
from netmiko import ConnectHandler
from getpass import getpass

username = input('enter your SSH username: ')
password = getpass()

with open('commands_file.txt') as f:
    commands_to_send = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()


for device in devices_list:
    print(f'connecting to {device}')
    ip_address_device = device
    ios_devices = {
    'device_type': 'cisco_ios',
    'ip': device,
    'username': username,
    'password': password,
    }
    
    net_connect = ConnectHandler(**ios_devices)
    output = net_connect.send_config_set(commands_to_send)
    print (output) 