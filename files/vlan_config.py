
# Generate vlan config and write to text file

vlan_file = open("vlan_config_data.txt", "w")

for vlan_id in range(2,11):
    vlan_file.write(f"vlan {vlan_id} \n")
    vlan_file.write(f"  name vlan_{ vlan_id } \n")

vlan_file.close() # Closing the write so we can use read

file_data = open("vlan_config_data.txt", "r")
# temp_var = file_data.read()
# temp_var = file_data.readline()
temp_var = file_data.readlines()
for v in temp_var:
    print(v)
#print(temp_var)