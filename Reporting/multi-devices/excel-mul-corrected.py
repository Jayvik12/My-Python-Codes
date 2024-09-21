import re
import os
import openpyxl
import yaml
from netmiko import ConnectHandler

# Load device details from YAML file
with open('device-detail-copy.yml', 'r') as yaml_file:
    device_data = yaml.safe_load(yaml_file)

routers = device_data['routers']

# Fetch username and password from environment variables (or set defaults for testing)
user = os.getenv('USERNAME')
user_password = os.getenv('PASSWORD')

# Create an Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Interface Status"

# Write the header row in the Excel file
header = ["Router", "Interface", "IP-Address", "OK?", "Method", "Status", "Protocol"]
ws.append(header)

# Regular expression to match the output format of 'show ip interface brief'
pattern = re.compile(r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(administratively\sdown|up|down)\s+(\S+)")

# Iterate over the routers and get the interface status
for router in routers:
    try:
        print(f"Connecting to {router['host']}...")
        
        # Establish connection to the router
        net_connect = ConnectHandler(
            device_type=router['device_type'],
            host=router['host'],
            username=user,
            password=user_password,
            secret=router['secret']
        )
        
        net_connect.enable()  # Enter enable mode
        
        # Execute the command 'show ip interface brief'
        output = net_connect.send_command('show ip interface brief')
        print(f"Interface Status for Router {router['host']}:\n", output)
        
        # Parse the output using regex and write to the Excel sheet
        for line in output.splitlines()[1:]:  # Skip the header line
            match = pattern.match(line)
            if match:
                interface_data = [router['host']] + list(match.groups())  # Prepend the router's IP/hostname to the row
                ws.append(interface_data)  # Append the row to the Excel sheet
        
        net_connect.disconnect()  # Disconnect after completing the task
    
    except Exception as e:
        print(f"Failed to connect to {router['host']}: {e}")

# Save the Excel file
wb.save("interface_status_new.xlsx")
print("Interface status has been saved to 'interface_status_new.xlsx'.")
