from napalm import get_network_driver

device_info = {
    "device_type": "cisco_ios",
    "host": "192.168.231.139",  # Replace with your switch's IP address
    "username": "netg",    # Replace with your username
    "password": "netg",  # Replace with your password
}

# Use the Cisco IOS driver
driver = get_network_driver('ios')