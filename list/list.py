#print("This is a list class")
#device_info[::-1] -- to reverse the list/string -- slicing
device_list = ['R1', 'R2', 'R3' ]

vlan_ids = [10, 20, 30, 40]

os_ver = [15.5, 15.6, 16.6]

os_vers = ['ios_15.5', 'ios_16.6']

device_info = ["switch", 10, 15.5, "23-06-2025", 'Cisco' ]


for item in device_info:
    print (item)
    
for i in device_list:
    newlist.append(i)
    print(newlist)

newlist = []

newlist.extend(device_list)

