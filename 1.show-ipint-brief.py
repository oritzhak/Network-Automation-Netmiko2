from netmiko import ConnectHandler

device_sw = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'david',
    'password': 'cisco',
}

net_connect = ConnectHandler(**device_sw) # connect to device
output = net_connect.send_command('show ip int brief') #run this command
print(output) # show the result

