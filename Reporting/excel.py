import openpyxl
from netmiko import ConnectHandler
import datetime


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

# Parse the output (Skip the header)
lines = output.splitlines()[1:]  # Skip the header line
parsed_data = []

for line in lines:
    if line.strip():  # Ignore empty lines
        columns = line.split()  # Split each line into columns
        if len(columns) >= 6:  # Ensure line has enough columns
            parsed_data.append(columns[:6])  # Get the first six columns

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Interface Status"

# Write the header row
sheet.append(["Interface", "IP-Address", "OK?", "Method", "Status", "Protocol"])

# Write the parsed interface data to the Excel sheet
for row in parsed_data:
    sheet.append(row)

# Save the Excel file
wb.save("interface_status.xlsx")

print("Interface status has been saved to 'interface_status.xlsx'.")

# Disconnect the SSH session
net_connect.disconnect()