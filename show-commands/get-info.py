# import yaml
# from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler


cisco_switch = {
    "device_type": "cisco_ios",
    "host": "192.168.231.139",  # Replace with your switch's IP address
    "username": "netg",    # Replace with your username
    "password": "netg",  # Replace with your password
}


net_connect = ConnectHandler(**cisco_switch)
output = net_connect.send_command("sh ip int br", use_textfsm=True)
# output = net_connect.send_command("show running-config")
# output = net_connect.send_command("show vlan brief")
print(output)


# Check for any down or administratively down interfaces
for interface in output:
    intf_name = interface['interface']
    intf_status = interface['status']
    
    # If the interface is down or administratively down, unshut it
    if intf_status == 'down' or intf_status == 'administratively down':
        print(f"Interface {intf_name} is down. Sending 'no shutdown' command...")
        config_commands = [f"interface {intf_name}", "no shutdown"]
        net_connect.send_config_set(config_commands)
        print(f"Interface {intf_name} has been brought up.")