from netmiko import ConnectHandler

with open('commands_file.txt') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco',
}
ios_devices2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'david',
    'password': 'cisco',
}

all_devices = [ios_devices, ios_devices2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print (output) 