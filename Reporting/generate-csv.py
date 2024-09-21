"""
import csv
import re
from netmiko import ConnectHandler

# Device details (replace with your actual router details)
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.231.141',  # Replace with the IP of your router
    'username': 'netg',      # Replace with your router's username
    'password': 'netg',      # Replace with your router's password
    'secret': 'enable_password'  # Replace with your enable/secret password if needed
}

# Connect to the router
net_connect = ConnectHandler(**cisco_router)
net_connect.enable()  # Enter enable mode

# Execute the command 'show ip interface brief'
output = net_connect.send_command('show ip interface brief')
print("Interface Status Output:\n", output)

# Regular expression to match the output format and handle "administratively down" as one entity
pattern = re.compile(r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(administratively\sdown|up|down)\s+(\S+)")

# List to store the parsed data
parsed_data = []

# Parse the output and match the regex pattern
for line in output.splitlines()[1:]:  # Skip the header line
    match = pattern.match(line)
    if match:
        parsed_data.append(match.groups())  # Add the matched groups to the parsed_data list

# Write to a CSV file
csv_file = 'interface_status_beautified.csv'

with open(csv_file, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write the header
    csv_writer.writerow(["Interface", "IP-Address", "OK?", "Method", "Status", "Protocol"])
    
    # Write the parsed data to the CSV file
    for row in parsed_data:
        csv_writer.writerow(row)

print(f"Interface status has been saved to '{csv_file}'.")

# Disconnect from the device
net_connect.disconnect()

""" 
import csv
import re
from netmiko import ConnectHandler


# Device details (replace with your actual details)
cisco_router = {
    'device_type': 'cisco_ios',  # Device type for Cisco IOS
    'host': '192.168.231.141',       # Replace with the IP of your router
    'username': 'netg',          # Replace with your router's username
    'password': 'netg',          # Replace with your router's password
    'secret': 'enable_password', # Replace with your enable/secret password if required
}

# Connect to the Cisco router
try:
    net_connect = ConnectHandler(**cisco_router)
    net_connect.enable()  # Enter enable mode if required

    # Run the 'show ip interface brief' command
    output = net_connect.send_command('show ip interface brief')
    print("Interface Status Output:\n", output)

    # Parse the output (Skip the header)
    lines = output.splitlines()[1:]  # Skip the header line
    parsed_data = []

    for line in lines:
        if line.strip():  # Ignore empty lines
            columns = line.split()  # Split each line into columns
            if len(columns) >= 6:  # Ensure valid line with enough columns
                parsed_data.append(columns[:6])  # Get the first six columns
    
    # Save the output to a CSV file
    with open('interface_status.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(["Interface", "IP-Address", "OK?", "Method", "Status", "Protocol"])
        # Write parsed rows
        csv_writer.writerows(parsed_data)

    print("Interface status has been saved to 'interface_status.csv'.")

finally:
    # Disconnect the SSH session
    net_connect.disconnect()

 

